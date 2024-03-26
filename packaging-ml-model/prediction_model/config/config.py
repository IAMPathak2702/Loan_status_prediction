import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent # take me to __init__.py file | Getting the parent Path...

DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"

SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT , 'trained_models')
MODEL_NAME = "Classification.pkl"
TARGET = "LoanAmount"

# Final Features used in Model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']


NUMERICAL_FEATURES = ['ApplicantIncome', 'CoapplicantIncome','Loan_Amount_Term']

CATEGORICAL_FEATURES =['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed','Property_Area']

NUMERICAL_CATEGORICAL_FEATURES=['Credit_History']



FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed','Property_Area','Credit_History']

FEATURES_TO_MODIFY = ["ApplicantIncome"]
FEATURES_TO_ADD = ["CoappliacantIncome"] 

COLUMN_TRANSFORM = ['Dependents']

DROP_FEATURES = ['Loan_ID','CoapplicationAmount']

LOG_FEATURES = ['ApplicantIncome', 'CoapplicantIncome','Loan_Amount_Term']