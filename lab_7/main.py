from dal.api_repository import APIRepository
from bll.data_service import DataService
from lab_7.ui.console_ui import ConsoleUI

class Command:
    def execute(self):
        base_url = "https://jsonplaceholder.typicode.com"
        repository = APIRepository(base_url)
        data_service = DataService(repository)
        console = ConsoleUI(data_service)
        console.run()
