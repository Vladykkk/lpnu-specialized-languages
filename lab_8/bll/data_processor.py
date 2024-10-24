import pandas as pd

class DataProcessor:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def get_extreme_values(self):
        return self.data.describe()

    def preprocess_data(self):
        self.data = self.data.dropna()
        return self.data
