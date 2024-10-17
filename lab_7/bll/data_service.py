from dal.api_repository import APIRepository

class DataService:
    def __init__(self, repository: APIRepository):
        self.repository = repository

    def fetch_and_display_data(self, endpoint):
        data = self.repository.get_data(endpoint)
        return data

    def save_data(self, data, format, filename):
        if format == "json":
            self.repository.save_as_json(data, filename)
        elif format == "csv":
            self.repository.save_as_csv(data, filename)
        elif format == "txt":
            self.repository.save_as_txt(data, filename)
        else:
            raise ValueError("Unsupported format")
