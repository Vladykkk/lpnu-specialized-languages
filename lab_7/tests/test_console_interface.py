from colorama import Fore

class ConsoleInterface:
    def __init__(self, data_service):
        self.data_service = data_service

    def run(self):
        while True:
            choice = input(Fore.CYAN + "Choose an option: ")
            if choice == "exit":
                print("Exiting...")
                break
            elif choice == "valid_option":
                data = self.data_service.fetch_and_display_data(choice)
                print(data)
            else:
                print("Invalid option. Please try again.")
