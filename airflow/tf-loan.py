from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import os
import pandas as pd
from keras.utils import FeatureSpace
import keras

def prepare_data(datapath:str):
    NUMERICAL_FEATURES = ['ApplicantIncome', 'CoapplicantIncome', 'Loan_Amount_Term']
    CATEGORICAL_FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']
    NUMERICAL_CATEGORICAL_FEATURES = ['Credit_History']
    LABEL_KEY = 'LoanAmount'
    COLUMNS_TO_DROP = ["Loan_ID"]

    # Read data
    df = pd.read_csv(datapath)

    # Drop unnecessary columns
    df.drop(COLUMNS_TO_DROP, axis=1, inplace=True)

    # Replace missing values
    for column in NUMERICAL_FEATURES + NUMERICAL_CATEGORICAL_FEATURES:
        df[column].fillna(df[column].median(), inplace=True)

    for column in CATEGORICAL_FEATURES:
        df[column].fillna(df[column].mode()[0], inplace=True)

    # Additional transformations
    df["Dependents"] = df["Dependents"].replace("3+", "3").astype(int)
    df["ApplicantIncome"] = df["ApplicantIncome"].astype(float)

    # Train-test split
    traindf, valdf = train_test_split(df)

    # Save to CSV
    df.to_csv('storage/loan_data/temp/df.csv', index=False)

def create_dataset_and_train_model(filepath:str):
    ds = pd.read_csv(filepath)
    train_df,val_df = train_test_split(ds)
    train_label = train_df.pop("LoanAmount")  # Extract labels and remove from features
    test_label = val_df.pop("LoanAmount")  # Extract labels and remove from features
    train_dataset = tf.data.Dataset.from_tensor_slices((dict(train_df), train_label))
    val_dataset = tf.data.Dataset.from_tensor_slices((dict(val_df), test_label))
    
    train_dataset = train_dataset.prefetch(tf.data.AUTOTUNE).batch(32)
    val_dataset=val_dataset.prefetch(tf.data.AUTOTUNE).batch(32)
   
    # Create the FeatureSpace object
    feature_space = FeatureSpace(
        features={
            'Gender': "string_categorical",
            'Married': "string_categorical",
            'Dependents': "integer_categorical",
            'Education': "string_categorical",
            'Self_Employed': "string_categorical",
            'ApplicantIncome': "float_normalized",
            'CoapplicantIncome': "float_normalized",
            'Loan_Amount_Term': "float_normalized",
            'Credit_History': "float_normalized",
            'Property_Area': "string_categorical",
            'Loan_Status': "string_categorical"
        }
    )
    
    
    # Adapt the FeatureSpace object to the dataset
    processed_train_ds = train_dataset.map(lambda x,_: x)
    feature_space.adapt(processed_train_ds)

    # Get the inputs and encoded features from the FeatureSpace object
    dict_inputs = feature_space.get_inputs()
    encoded_feature = feature_space.get_encoded_features()

    # Construct your neural network model
    x = keras.layers.Dense(32, activation='relu')(encoded_feature)
    x = keras.layers.Dense(64, activation='relu')(x)
    x = keras.layers.Dropout(0.5)(x)
    output = keras.layers.Dense(1, activation="relu")(x)

    # Create the model
    model = keras.models.Model(inputs=dict_inputs, outputs=output)

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae', 'mse'])
    history = model.fit(train_dataset,
                    epochs = 20,
                    validation_data=val_dataset)
    
    
# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('Loan-Airflow',
          default_args=default_args,
          description='Train TensorFlow model for Loan Amount Prediction',
          schedule_interval=None,
          )

# Define tasks
preprocess_task = PythonOperator(
    task_id='preprocess',
    python_callable=prepare_data,
    op_args=['storage/data/loan-data/loan_data_set.csv'],
    dag=dag,
)

train_task = PythonOperator(
    task_id='train',
    python_callable=create_dataset_and_train_model,
    op_args=['storage/loan_data/temp/df.csv'],
    dag=dag,
)

# Set task dependencies
preprocess_task >> train_task