> # Stock Price Prediction API

## **System Requirements**
```
- Python 3.10 or latest
- pip 
```

## **Installation**

### **1. Project structure**
```
prices/
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── models/
│   ├── __init__.py
│   └── model_loader.py
│
├── services/
│   ├── __init__.py
│   ├── data_service.py
│   └── prediction_service.py
│
├── utils/
│   ├── __init__.py
│   ├── data_preprocessor.py
│   └── scaler.py
│
├── app.py
├── Dockerfile
├── Readme.md
└── requirements.txt
```

### **2. Install the dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the app**
```bash
# for development
python app.py

# or
flask run
```

## **Endpoints**
```
/prices
/prices/<crypto_id>
```

## **Docker Container**

### 1. Build the Docker image :
```
docker build -t stock-prediction-api .
```
### 2. Run the container:
```
docker run -p 8080:8080 stock-prediction-api
```
The API will be accessible at http://localhost:8080