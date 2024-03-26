from sklearn.pipeline import Pipeline
from prediction_model.config import config
from prediction_model.processing import preprocessing as pp 
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

classification_pipeline = Pipeline(
    [
        ('DomainProcessing',pp.DomainProcessor(variables_to_modify = config.FEATURES_TO_MODIFY,
        variable_to_add = config.FEATURES_TO_ADD)),
        ('MeanImputation', pp.MeanImputer(variables=config.NUMERICAL_FEATURES)),
        ('ModeImputation',pp.ModeImputer(variables=config.CATEGORICAL_FEATURES)),
        ('DropFeatures', pp.DropColumns(variables_to_drop=config.DROP_FEATURES)),
        ("ColumnTransform",pp.ColumnTransformer(variables=config.COLUMN_TRANSFORM)),
        ('LabelEncoder',pp.CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)),
        ('LogTransform',pp.LogTransformer(variables=config.LOG_FEATURES)),
        ('MinMaxScale', MinMaxScaler()),
        ('LogisticClassifier',LogisticRegression(random_state=0))
    ]
)