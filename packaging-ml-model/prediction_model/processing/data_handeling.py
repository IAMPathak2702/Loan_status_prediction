import os
import pandas as pd
import joblib

from prediction_model.config import config


# Load the dataset
def load_dataset(filename):
    filepath = os.path.join(config.DATAPATH, filename)
    _data = pd.read_csv(filename)
    return _data


# serialise the model
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print(f"Model has been saved under the name :- {config.MODEL_NAME}")


# deserialize the model
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    model_loaded = joblib.load(pipeline_to_load, save_path)
    print(f"Model has been Loaded")
