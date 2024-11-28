from bll.data_service import DataService
from tabulate import tabulate
import colorama
from colorama import Fore

colorama.init(autoreset=True)

class ConsoleUI:
    def __init__(self, data_service: DataService):
        self.data_service = data_service

    def display_menu(self):
        print(Fore.YELLOW + "1. Отримати та відобразити дані")
        print(Fore.YELLOW + "2. Зберегти дані у файл")
        print(Fore.YELLOW + "3. Вийти")

    def fetch_and_display(self):
        endpoint = input(Fore.CYAN + "Введіть API-ендпоінт (наприклад, posts): ")
        data = self.data_service.fetch_and_display_data(endpoint)
        if data:
            print(tabulate(data, headers="keys", tablefmt="grid"))

    def save_data(self):
        endpoint = input(Fore.CYAN + "Введіть API-ендпоінт (наприклад, posts): ")
        data = self.data_service.fetch_and_display_data(endpoint)
        if data:
            format = input(Fore.CYAN + "Введіть формат (json/csv/txt): ")
            filename = input(Fore.CYAN + "Введіть ім'я файлу: ")
            self.data_service.save_data(data, format, filename)
            print(Fore.GREEN + f"Дані збережено у файл {filename}.")

    def run(self):
        while True:
            self.display_menu()
            choice = input(Fore.CYAN + "Оберіть опцію: ")
            if choice == "1":
                self.fetch_and_display()
            elif choice == "2":
                self.save_data()
            elif choice == "3":
                print(Fore.GREEN + "До побачення!")
                break
            else:
                print(Fore.RED + "Неправильний вибір. Спробуйте ще раз.")
