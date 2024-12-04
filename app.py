import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.model_loader import ModelLoader
from config.config import MODEL_URL, MODEL_CONFIG, CSV_URLS, COIN_NAMES
from services.data_service import DataService
from services.prediction_service import PredictionService
from utils.scaler import PriceScaler
from flask import Flask, jsonify

app = Flask(__name__)

# Load model at startup
model = ModelLoader.download_and_load_model(MODEL_URL)
scaler = PriceScaler()

@app.route('/prices', methods=['GET'])
def get_all_prices():
    try:
        # List to store prices for all cryptocurrencies
        all_crypto_prices = []
        for crypto_id in CSV_URLS:
            try:
                id = crypto_id.lower()
                coin_name = COIN_NAMES.get(id, id.capitalize())
                prices, times, volumes, market_caps = DataService.get_data_for_crypto(id)
                
                latest_price = float(prices[-1])
                previous_price = float(prices[-2]) if len(prices) > 1 else latest_price
                
                short_term_percentage_change = round(((latest_price - previous_price) / previous_price) * 100, 2)
                
                crypto_info = {
                    "coin": coin_name,
                    "coin symbol": id.upper(),
                    "current price": "{:,.2f}".format(latest_price),
                    "percentage": short_term_percentage_change
                }
                
                all_crypto_prices.append(crypto_info)
            
            except Exception as crypto_error:
                print(f"Error processing {id}: {crypto_error}")
                continue
        
        return jsonify(all_crypto_prices)
    
    except Exception as e:
        print(f"Unexpected Error in get_all_prices: {e}")
        return jsonify({"error": "An unexpected error occurred while fetching prices"}), 500

@app.route('/prices/<id>', methods=['GET'])
def get_prices(id):
    try:
        # Normalize the ID to lowercase
        id = id.lower()
        
        # Validate if coin exists in CSV_URLS
        if id not in CSV_URLS:
            return jsonify({"error": "Cryptocurrency not found"}), 404
        
        # Get coin name from COIN_NAMES, fallback to capitalized ID
        coin_name = COIN_NAMES.get(id, id.capitalize())
        
        # Get data for specified cryptocurrency
        prices, times, volumes, market_caps = DataService.get_data_for_crypto(id)
        
        # Scale prices
        scaled_prices = scaler.fit_transform(prices)
        
        # Actual prices
        actual_prices = [
            {
                "time": t[0], 
                "value": "{:,.2f}".format(float(v)) 
            } for t, v in zip(times, prices.flatten())
        ]
        
        # Generate predictions
        predicted_prices, future_predicted_prices = PredictionService.generate_predictions(
            model, scaled_prices, scaler, times
        )
        predicted_prices = [
            {
                "time": p["time"], 
                "value": "{:,.2f}".format(float(p["value"]))
            } for p in predicted_prices
        ]
        future_predicted_prices = [
            {
                "time": p["time"], 
                "value": "{:,.2f}".format(float(p["value"]))
            } for p in future_predicted_prices
        ]
        
        # Calculate latest price and percentage change
        latest_price = float(actual_prices[-1]['value'].replace(',', ''))
        previous_price = float(actual_prices[-2]['value'].replace(',', '')) if len(actual_prices) > 1 else latest_price
        short_term_percentage_change = round(((latest_price - previous_price) / previous_price) * 100)
        
        # Calculate 12-month (Yearly) Price Change
        if len(actual_prices) >= 12:
            yearly_start_price = float(actual_prices[-12]['value'].replace(',', ''))
            yearly_percentage_change = round(((latest_price - yearly_start_price) / yearly_start_price) * 100)
        else:
            yearly_percentage_change = None
            
        # get value of volume & marketCap
        latest_volume = "{:,.0f}".format(float(volumes[-2]))
        latest_marketcap = "{:,.0f}".format(float(market_caps[-2]))
        
        # Prepare response
        response = {
            "coin": coin_name,
            "coin symbol": id.upper(),
            "prediction chart" : {
                "actual price": actual_prices,
                "history predicted": predicted_prices,
                "future prediction": future_predicted_prices
            },
            "current price": "{:,.2f}".format(latest_price),
            "percentage": short_term_percentage_change,
            "yearly percentage": yearly_percentage_change,
            "volume": latest_volume,
            "marketcap": latest_marketcap
        }
        
        return jsonify(response)
    
    except ValueError as e:
        print(f"ValueError: {e}") 
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        print(f"Unexpected Error: {e}") 
        return jsonify({"error": "An unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=3000, host='0.0.0.0')