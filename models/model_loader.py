import requests
from tensorflow.keras.models import load_model
import os

class ModelLoader:
    @staticmethod
    def download_and_load_model(model_url, local_path='model.h5'):
        # Download model from cloud storage
        response = requests.get(model_url)
        with open(local_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Model downloaded from cloud storage and saved as {local_path}")
        model = load_model(local_path)
        print("Model loaded successfully.")
        
        return model
