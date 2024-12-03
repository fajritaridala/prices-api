from config.config import CSV_URLS
from utils.data_preprocessor import DataPreprocessor

class DataService:
    @classmethod
    def get_data_for_crypto(cls, crypto_id):
        # Validate cryptocurrency ID
        csv_url = CSV_URLS.get(crypto_id.lower())
        if not csv_url:
            raise ValueError(f"Invalid cryptocurrency ID. Supported IDs are: {', '.join(CSV_URLS.keys())}")
        
        # Load and return data
        return DataPreprocessor.load_data_from_url(csv_url)
