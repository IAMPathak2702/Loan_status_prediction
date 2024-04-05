import pathlib
import os
import prediction_model

# Set up paths
PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent
DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")
TRAIN_FILE = os.path.join(DATAPATH, "train.csv")
TEST_FILE = os.path.join(DATAPATH, "test.csv")
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, 'trained_models')

# Model configuration
MODEL_NAME = 'classification.pkl'
TARGET = 'Loan_Status'

# Features used in the model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']

# Feature types
NUMERICAL_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
CATEGORICAL_FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
                        'Self_Employed', 'Property_Area', 'Credit_History']
FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education',
                      'Self_Employed', 'Property_Area', 'Credit_History']
FEATURES_TO_MODIFY = ["ApplicantIncome"]
FEATURES_TO_ADD = "CoapplicantIncome"
COLUMN_TRANSFORM = ['Dependents']
DROP_FEATURES = ['CoapplicantIncome']
LOG_FEATURES = ['ApplicantIncome', 'LoanAmount'] # taking log of numerical columns
