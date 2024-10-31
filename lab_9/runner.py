from lab_2.main import run as run_lab2

class Runner:
    def __init__(self):
        self.labs = {
            "2": run_lab2,
        }

    def display_menu(self):
        print("\nМеню запуску лабораторних робіт:")
        for lab_num in sorted(self.labs.keys()):
            print(f"{lab_num}. Лабораторна робота {lab_num}")
        print("q. Вихід")

    def run_lab(self, lab_number):
        lab = self.labs.get(lab_number)
        if lab:
            print(f"\nЗапускаємо Лабораторну роботу {lab_number}...\n")
            lab()
        else:
            print("Неправильний номер лабораторної роботи. Спробуйте ще раз.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nОберіть номер лабораторної роботи або 'q' для виходу: ").strip()
            
            if choice == 'q':
                print("Дякуємо за використання!")
                break
            else:
                self.run_lab(choice)
