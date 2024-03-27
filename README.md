# Loan Status Prediction Pipeline

This repository contains a loan status prediction pipeline built using TensorFlow Extended (TFX),Kubeflow and Airflow.

## Overview

The loan status prediction pipeline aims to predict whether a loan applicant will default or not based on various features such as credit score, income, loan amount, etc. The pipeline consists of the following main components:

1. Data Ingestion: Raw data is ingested from various sources and stored in a centralized data store (e.g., Google Cloud Storage, Amazon S3).
2. Data Validation and Transformation: Data is validated for inconsistencies and transformed into a format suitable for model training.
3. Model Training: Several machine learning models are trained using the preprocessed data.
4. Model Evaluation: The trained models are evaluated on a held-out validation dataset to assess their performance.
5. Model Deployment: The best-performing model is deployed to a serving infrastructure to make predictions.

## Pipeline Components

### 1. TFX Components

TFX provides several components that are used in the pipeline:

- **ExampleGen**: Responsible for ingesting and splitting the input data into training and evaluation sets.
- **StatisticsGen**: Computes statistics over the dataset for visualization and data analysis.
- **SchemaGen**: Generates a schema based on the computed statistics to define the expected data format.
- **ExampleValidator**: Validates the data against the generated schema to detect and fix anomalies.
- **Transform**: Performs feature engineering and preprocessing on the dataset.
- **Trainer**: Trains machine learning models on the preprocessed data.
- **Evaluator**: Evaluates the trained models using a held-out evaluation dataset.
- **Pusher**: Deploys the best-performing model to a serving infrastructure.

# Loan Status Prediction Model Tree


## Overview
This project contains a machine learning pipeline for predicting loan status. The pipeline includes preprocessing steps, feature engineering, and a logistic regression classifier.

## Custom Transformers
We have implemented several custom transformers for preprocessing the data:

### MeanImputer
- Fills missing values with the mean of the column.

### ModeImputer
- Fills missing values with the mode of the column.

### DropColumns
- Drops specified columns from the DataFrame.

### DomainProcessor
- Modifies domain-specific features by adding values from another column.

### CustomLabelEncoder
- Encodes categorical variables with custom logic.

### LogTransformer
- Applies a logarithmic transformation to specified columns.

### ColumnTransformer (Custom)
- Performs custom transformations on specified columns, such as replacing '3+' with '3'.

## Pipeline Configuration
The pipeline is configured with the following steps:
1. Domain processing
2. Mean imputation for numerical features
3. Mode imputation for categorical features
4. Dropping unnecessary features
5. Custom column transformation
6. Label encoding for categorical features
7. Log transformation for numerical features
8. Min-Max scaling
9. Logistic regression classification

## Model Training and Serialization
The `perform_training` function is responsible for training the model using the pipeline and saving the trained model to disk.

## Data Handling
Utility functions are provided for loading datasets and saving/loading the serialized model.

## Usage
To train the model, navigate to the model's directory and run the `training_pipeline.py` script:

```shell
python training_pipeline.py
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Snapshots of the projects
<img src=https://raw.githubusercontent.com/IAMPathak2702/Loan_status_prediction-TFX-pipeline/main/images/history_model.png>
<img src=https://raw.githubusercontent.com/IAMPathak2702/Loan_status_prediction-TFX-pipeline/main/images/model%20png.png>

```bash
tree -o readme.md
```
Loan_status_prediction-TFX-pipeline/ ├── packaging-ml-model/ │ ├── prediction_model/ │ │ ├── init.py │ │ ├── config.py │ │ ├── datasets/ │ │ │ ├── train.csv │ │ │ └── test.csv │ │ ├── processing/ │ │ │ ├── data_handling.py │ │ │ ├── preprocessing.py │ │ │ └── init.py │ │ ├── trained_models/ │ │ │ └── classification.pkl │ │ ├── pipeline.py │ │ └── training_pipeline.py │ └── README.md └── .gitignore
