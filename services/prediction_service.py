import numpy as np
import pandas as pd
from config.config import MODEL_CONFIG

class PredictionService:
    @classmethod
    def generate_predictions(cls, model, scaled_prices, scaler, times):
        # Historical predictions
        sequence_length = MODEL_CONFIG['sequence_length']
        test_data = scaled_prices[-(sequence_length + 30):]
        x_test = cls._prepare_test_data(test_data, sequence_length)
        
        predictions = model.predict(x_test)
        predictions = scaler.inverse_transform(predictions)
        
        # Predicted prices for test set
        predicted_prices = [
            {"time": times[-len(predictions) + i][0], "value": float(v)} 
            for i, v in enumerate(predictions.flatten())
        ]
        
        # Future predictions
        future_predictions = cls._generate_future_predictions(
            model, scaled_prices, scaler, sequence_length
        )
        
        # Generate future dates
        future_dates = cls._generate_future_dates(times)
        
        future_predicted_prices = [
            {"time": t, "value": float(v)} 
            for t, v in zip(future_dates, future_predictions)
        ]
        
        return predicted_prices, future_predicted_prices
    
    @staticmethod
    def _prepare_test_data(test_data, sequence_length):
        x_test = []
        for i in range(sequence_length, len(test_data)):
            x_test.append(test_data[i-sequence_length:i, 0])
        
        x_test = np.array(x_test)
        return np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    
    @staticmethod
    def _generate_future_predictions(model, scaled_prices, scaler, sequence_length, month=12):
        future_predictions = []
        input_sequence = scaled_prices[-sequence_length:]
        
        for _ in range(month):
            input_sequence_reshaped = input_sequence.reshape(1, sequence_length, 1)
            next_price_scaled = model.predict(input_sequence_reshaped)
            future_predictions.append(scaler.inverse_transform(next_price_scaled)[0, 0])
            input_sequence = np.append(input_sequence, next_price_scaled)[-sequence_length:]
        
        return future_predictions
    
    @staticmethod
    def _generate_future_dates(times):
        df = pd.DataFrame(times, columns=['date'])
        df['diff'] = df['date'].diff()
        most_common_diff = df['diff'].mode()[0]
        last_timestamp = df['date'].iloc[-1]
        
        return [last_timestamp + i * most_common_diff for i in range(1, 11)]
