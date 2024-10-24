import pandas as pd

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        try:
            data = pd.read_csv(self.file_path)
            return data
        except FileNotFoundError:
            print("CSV-файл не знайдено. Повертається порожній DataFrame.")
            return pd.DataFrame()
