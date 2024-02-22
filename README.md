# Loan Status Prediction Pipeline

This repository contains a loan status prediction pipeline built using TensorFlow Extended (TFX) and orchestrated with Kubeflow and Airflow.

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

### 2. Orchestrators

The pipeline is orchestrated using both Kubeflow and Airflow:

- **Kubeflow**: Orchestrates the execution of TFX components as Kubernetes pods. Provides scalability and manageability for running the pipeline on Kubernetes.
- **Airflow**: Manages the scheduling and execution of the pipeline components as Airflow DAGs. Allows for complex workflows and integration with external systems.

## Pipeline Execution

The pipeline can be executed as follows:

1. Set up a Kubernetes cluster and install Kubeflow for orchestration.
2. Set up Airflow and configure it to communicate with Kubeflow.
3. Define the pipeline components using TFX DSL (Python scripts).
4. Create and configure the Airflow DAG to schedule and execute the pipeline components.
5. Run the Airflow DAG to trigger the pipeline execution.
6. Monitor the pipeline execution using Kubeflow and Airflow UIs.
7. Deploy the trained model for serving once the pipeline completes successfully.

## Requirements

- Kubernetes cluster
- Kubeflow
- Airflow
- TensorFlow Extended (TFX)
- Python 3.x
- Google Cloud SDK (optional, for cloud-based data storage and processing)
- Docker (for building custom TFX components)
- Other dependencies as specified in the requirements.txt file

## Contributing

Contributions to the pipeline are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
