import requests
import tempfile
from tensorflow.keras.models import load_model
import os

class ModelLoader:
    @staticmethod
    def download_and_load_model(model_url):
        try:
            # Download model from cloud storage
            response = requests.get(model_url)
            
            # use tempfile to temporary saving
            with tempfile.NamedTemporaryFile(delete=False, suffix='.h5') as temp_file:
                temp_file.write(response.content)
                temp_file_path = temp_file.name
            
            # Load model from tempfile
            model = load_model(temp_file_path)
            
            # delete temporary file 
            os.unlink(temp_file_path)
            
            print("Model loaded successfully from cloud storage.")
            
            return model
        
        except Exception as e:
            print(f"Error loading model: {e}")
            raise