from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from prediction_model.config import config
import pandas as pd
class MeanImputer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables
        
    def fit(self, X, y=None):
        self.mean_dict = {}
        for col in self.variables:
            self.mean_dict[col] = X[col].mean()
        return self
        
    def transform(self, X):
        X_transformed = X.copy()
        for col in self.variables:
            mean_value_formatted = "{:.2f}".format(self.mean_dict[col])
            X_transformed[col].fillna(mean_value_formatted, inplace=True)
        return X_transformed
    
    
class ModeImputer(BaseEstimator,TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables
        
    def fit(self, X, y=None):
        self.mode_dict = {}
        for col in self.variables:
            self.mode_dict[col] = X[col].mode()[0]
        return self
        
    def transform(self, X):
        X_transformed = X.copy()
        for col in self.variables:
            mode_value = self.mode_dict[col]
            X_transformed[col].fillna(mode_value, inplace=True)
        return X_transformed
    

from sklearn.base import BaseEstimator, TransformerMixin

class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):
        self.variables_to_drop = variables_to_drop
        
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        X_transformed = X.drop(columns=self.variables_to_drop, axis=1)        
        return X_transformed



class DomainProcessor(BaseEstimator,TransformerMixin):
    def __init__(self,variable_to_modify = None, variable_to_add = None):
        self.variable_to_modify = variable_to_modify
        self.variable_to_add = variable_to_add
    
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        X = X.copy()
        for feature in self.variable_to_modify:
            X[feature] = X[feature] + X[self.variable_to_add]
        return X

class CustomLabelEncoder(BaseEstimator,TransformerMixin):
    def __init__(self, variables=None):
        self.variables=variables
    
    def fit(self, X,y):
        self.label_dict = {}
        for var in self.variables:
            t = X[var].value_counts().sort_values(ascending=True).index 
            self.label_dict[var] = {k:i for i,k in enumerate(t,0)}
        return self
    
    def transform(self,X):
        X=X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.label_dict[feature])
        return X


# Log Transformation
class LogTransformer(BaseEstimator,TransformerMixin):
    def __init__(self,variables=None):
        self.variables = variables
    
    def fit(self,X,y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            # Convert to numeric and handle non-numeric values
            X[col] = pd.to_numeric(X[col], errors='coerce')
            # Drop NaN values
            X[col].dropna(inplace=True)
            # Apply log transformation
            X[col] = np.log(X[col])
        return X

class ColumnTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, variables=None):
        self.variables = variables
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.variables:
            X[col] = X[col].replace('3+', '3')
        return X
