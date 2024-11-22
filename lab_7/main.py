from dal.api_repository import APIRepository
from bll.data_service import DataService
from ui.console_interface import ConsoleInterface

class Lab7Command:
    def execute(self):
        base_url = "https://jsonplaceholder.typicode.com"
        repository = APIRepository(base_url)
        data_service = DataService(repository)
        console = ConsoleInterface(data_service)
        console.run()
