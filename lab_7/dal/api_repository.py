import requests
import json
import csv

class APIRepository:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error fetching data from API: {e}")

    def save_as_json(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def save_as_csv(self, data, filename):
        keys = data[0].keys()
        with open(filename, 'w', newline='') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

    def save_as_txt(self, data, filename):
        with open(filename, 'w') as f:
            for item in data:
                f.write(f"{item}\n")
