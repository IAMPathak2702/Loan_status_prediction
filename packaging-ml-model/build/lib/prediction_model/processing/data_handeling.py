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
    try:
        save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
        joblib.dump(pipeline_to_save, save_path)
        print(f"Model has been saved under the name :- {config.MODEL_NAME}")
    except Exception as e:
        print(f"Error saving pipeline from {save_path}: {e}")
        return None

# deserialize the model
def load_pipeline(model_name):
    try: 
        save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
        model_loaded = joblib.load(save_path)
        print(f"Model has been loaded")
        return model_loaded
    except Exception as e:
        print(f"Error loading pipeline from {model_name}: {e}")
        return None
