from google.cloud import firestore

def get_crypto_configs_from_firestore():
    try:
        db = firestore.Client()
        cryptocurrencies_ref = db.collection('cryptocurrencies')
        docs = cryptocurrencies_ref.stream()
        
        crypto_configs = {}
        for doc in docs:
            config = doc.to_dict()
            crypto_configs[config['coin_symbol'].lower()] = {
                'coin_symbol': config['coin_symbol'],
                'coin': config['coin'],
                'link_csv': config['link_csv']
            }
        
        return crypto_configs
    except Exception as e:
        print(f"Error accessing Firestore: {e}")
        return {}


# Ganti konfigurasi existing
crypto_configs = get_crypto_configs_from_firestore()
COIN_NAMES = {config['coin_symbol'].lower(): config['coin'] for config in crypto_configs.values()}
CSV_URLS = {config['coin_symbol'].lower(): config['link_csv'] for config in crypto_configs.values()}


# Configuration management
MODEL_URL = 'https://storage.googleapis.com/stock-market-model/BTC_model.h5'

MODEL_CONFIG = {
    'sequence_length': 10,
    'prediction_days': 10
}