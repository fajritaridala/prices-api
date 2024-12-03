# Configuration management
MODEL_URL = 'https://storage.googleapis.com/stock-market-model/BTC_model.h5'

COIN_NAMES = {
    "btc": "Bitcoin",
    "sol": "Solana",
    "sui": "Sui",
    "ena": "ENA",
    "eth": "Ethereum", 
    "op": "Optimism",
    "render": "Render",
    "tao": "Tao",
    "tia": "Celestia",
    "xrp": "Ripple"
}

CSV_URLS = {
    "btc": "https://storage.googleapis.com/stock-market-csv/BTC_All_graph_coinmarketcap.csv",
    "sol": "https://storage.googleapis.com/stock-market-csv/SOL_All_graph_coinmarketcap.csv",
    "sui": "https://storage.googleapis.com/stock-market-csv/SUI_All_graph_coinmarketcap.csv",
    "ena": "https://storage.googleapis.com/stock-market-csv/ENA_All_graph_coinmarketcap.csv",
    "eth": "https://storage.googleapis.com/stock-market-csv/ETH_All_graph_coinmarketcap.csv",
    "op": "https://storage.googleapis.com/stock-market-csv/OP_All_graph_coinmarketcap.csv",
    "render": "https://storage.googleapis.com/stock-market-csv/RENDER_All_graph_coinmarketcap.csv",
    "tao": "https://storage.googleapis.com/stock-market-csv/TAO_All_graph_coinmarketcap.csv",
    "tia": 'https://storage.googleapis.com/stock-market-csv/TIA_All_graph_coinmarketcap.csv',
    "xrp": "https://storage.googleapis.com/stock-market-csv/XRP_All_graph_coinmarketcap.csv"
}

MODEL_CONFIG = {
    'sequence_length': 10,
    'prediction_days': 10
}