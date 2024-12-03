# Stock Price Prediction API

## Persyaratan Sistem
- Python 3.11 or latest
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
└── app.py
```


### 2. Buat File `requirements.txt`
```
flask==2.1.0
tensorflow==2.9.0
numpy==1.22.4
pandas==1.4.2
scikit-learn==1.1.1
requests==2.27.1
```

### 3. Instal Dependensi
```bash
pip install -r requirements.txt
```

### 4. Menjalankan Aplikasi
```bash
# Untuk development
python app.py

# Atau
flask run
```

## Endpoints
```
/prices/<crypto_id>
```

request body :
```json
{
  "prediction chart" : {
    "actual price": "harga asli",
    "history predicted": "prediksi histori harga asli",
    "future prediction": "prediksi harga masa depan
  },
  "current price": "harga terkin",
  "percentage": "persentase 1 bulan terakhir",
  "yearly percentage": "persentase 1 tahun terakhir",
  "volume": "volume terbaru",
  "marketcap": "kapitalisasi pasar terbaru"
}
```
