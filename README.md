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


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Snapshots of the projects
<img src=https://raw.githubusercontent.com/IAMPathak2702/Loan_status_prediction-TFX-pipeline/main/images/history_model.png>
<img src=https://raw.githubusercontent.com/IAMPathak2702/Loan_status_prediction-TFX-pipeline/main/images/model%20png.png>

```bash
tree -o readme.md
```
