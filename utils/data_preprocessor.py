import numpy as np
import pandas as pd
import io
import requests

class DataPreprocessor:
    @staticmethod
    def load_data_from_url(csv_url):
        # Download and process data from URL
        response = requests.get(csv_url)
        data = pd.read_csv(io.StringIO(response.text), delimiter=';')
        
        # Extract prices and timestamps
        prices = data['close'].values.reshape(-1, 1)
        timestamp = data['timestamp'].values
        market_caps = data['marketCap'].values.reshape(-1,1)
        volumes = data['volume'].values

        # Convert timestamp to date
        df = pd.DataFrame(timestamp, columns=['timestamp'])
        df['date'] = pd.to_datetime(df['timestamp'], format='ISO8601').dt.date
        df = df.drop(columns=['timestamp'])
        times = np.array(df)
        
        return prices, times, volumes, market_caps
    
    @staticmethod
    def prepare_sequence_data(scaled_prices, sequence_length):
        x_data = []
        for i in range(sequence_length, len(scaled_prices)):
            x_data.append(scaled_prices[i-sequence_length:i, 0])
        
        x_data = np.array(x_data)
        x_data = np.reshape(x_data, (x_data.shape[0], x_data.shape[1], 1))
        
        return x_data
