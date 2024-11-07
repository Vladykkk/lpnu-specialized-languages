from lab_2.main import Lab2Runner

class RunnerFacade:
    def __init__(self):
        self.labs = {
            "2": Lab2Runner(),
        }

    def run_lab(self, lab_number):
        lab = self.labs.get(lab_number)
        if lab:
            lab.run()
        else:
            print("Невірний номер лабораторної роботи.")

    def display_menu(self):
        print("\nМеню запуску лабораторних робіт:")
        for number in self.labs.keys():
            print(f"Лабораторна робота №{number}")
        print("Введіть номер лабораторної роботи або 'q' для виходу.")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Ваш вибір: ")
            if choice.lower() == 'q':
                print("Вихід з програми.")
                break
            else:
                self.run_lab(choice)

if __name__ == "__main__":
    runner = RunnerFacade()
    runner.start()
