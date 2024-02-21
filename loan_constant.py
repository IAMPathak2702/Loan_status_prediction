
# Define the numerical features
NUMERICAL_FEATURES = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']

# Define the categorical numerical features
CATEGORICAL_NUMERICAL_FEATURES = ['Dependents']

# Define the categorical string features
CATEGORICAL_STRING_FEATURES = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']

# Number of vocabulary terms used for encoding categorical features.
VOCAB_SIZE = 1000

# Count of out-of-vocab buckets in which unrecognized categorical are hashed.
OOV_SIZE = 10

LABEL_KEY = 'Loan_Status'
