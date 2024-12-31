# Stock Price Prediction API

## Persyaratan Sistem
- Python 3.10 or latest
- pip

## Instalasi

### 1. Struktur Proyek
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

### 2. Instal Dependensi
```bash
pip install -r requirements.txt
```

### 3. Menjalankan Aplikasi
```bash
# Untuk development
python app.py

# Atau
flask run
```

## Endpoints
```
/prices
/prices/<crypto_id>
```