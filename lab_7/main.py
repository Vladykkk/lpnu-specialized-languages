from dal.api_repository import APIRepository
from bll.data_service import DataService
from ui.console_interface import ConsoleInterface

def main():
    base_url = "https://jsonplaceholder.typicode.com"
    repository = APIRepository(base_url)
    data_service = DataService(repository)
    console = ConsoleInterface(data_service)
    console.run()

if __name__ == "__main__":
    main()
