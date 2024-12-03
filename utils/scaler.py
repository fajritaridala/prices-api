from sklearn.preprocessing import MinMaxScaler

class PriceScaler:
    def __init__(self, feature_range=(0, 1)):
        self.scaler = MinMaxScaler(feature_range=feature_range)
    
    def fit_transform(self, data):
        return self.scaler.fit_transform(data)
    
    def inverse_transform(self, data):
        return self.scaler.inverse_transform(data)
