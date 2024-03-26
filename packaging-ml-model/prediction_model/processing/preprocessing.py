from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from prediction_model.config import config

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
    

class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_drop=None):
        self.variables_to_drop = variables_to_drop
        
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        X_transformed = X.copy()
        X_transformed = X_transformed.drop(columns=self.variables_to_drop)        
        return X_transformed


class DomainProcessor(BaseEstimator, TransformerMixin):
    def __init__(self, variables_to_modify=None, variable_to_add=None):
        self.variable = variables_to_modify
        self.reference_variable = variable_to_add
        
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        X_transformed = X.copy()
        X_transformed[self.variable] = X_transformed[self.variable] + X_transformed[self.reference_variable]
        return X_transformed

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
    
    def transform(self,X):
        X = X.copy()
        for col in self.variables:
            X[col] = np.log(X[col])
        return X

class ColumnTransformer(BaseEstimator,TransformerMixin):
    def __init__(self,variables=None):
        self.variables = variables
    
    def fit(self,X,y=None):
        return self
    
    def transform(self,X):
        X = X.copy()
        for col in self.variables:
            X[self.variables]=X[self.variables].replace('3+', '3')
        return X