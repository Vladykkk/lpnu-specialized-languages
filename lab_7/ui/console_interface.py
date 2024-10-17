from bll.data_service import DataService
from tabulate import tabulate
import colorama
from colorama import Fore

colorama.init(autoreset=True)

class ConsoleInterface:
    def __init__(self, data_service: DataService):
        self.data_service = data_service

    def display_menu(self):
        print(Fore.YELLOW + "1. Fetch and Display Data")
        print(Fore.YELLOW + "2. Save Data to File")
        print(Fore.YELLOW + "3. Exit")

    def fetch_and_display(self):
        endpoint = input(Fore.CYAN + "Enter API endpoint (e.g., posts): ")
        data = self.data_service.fetch_and_display_data(endpoint)
        if data:
            print(tabulate(data, headers="keys", tablefmt="grid"))

    def save_data(self):
        endpoint = input(Fore.CYAN + "Enter API endpoint (e.g., posts): ")
        data = self.data_service.fetch_and_display_data(endpoint)
        if data:
            format = input(Fore.CYAN + "Enter format (json/csv/txt): ")
            filename = input(Fore.CYAN + "Enter filename: ")
            self.data_service.save_data(data, format, filename)
            print(Fore.GREEN + f"Data saved to {filename}.")

    def run(self):
        while True:
            self.display_menu()
            choice = input(Fore.CYAN + "Choose an option: ")
            if choice == "1":
                self.fetch_and_display()
            elif choice == "2":
                self.save_data()
            elif choice == "3":
                print(Fore.GREEN + "Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid option. Please try again.")
