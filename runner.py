import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab_3"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab_4"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab_5"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab_7"))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lab_8"))

lab_3_venv_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "lab_3", "venv", "lib", "python3.13", "site-packages"
)
sys.path.append(lab_3_venv_path)

lab_5_venv_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "lab_5", "venv", "lib", "python3.13", "site-packages"
)
sys.path.append(lab_5_venv_path)

lab_7_venv_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "lab_7", "venv", "lib", "python3.13", "site-packages"
)
sys.path.append(lab_7_venv_path)

lab_8_venv_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "lab_8", "venv", "lib", "python3.13", "site-packages"
)
sys.path.append(lab_8_venv_path)

from lab_1.main import Command as Lab1Command
from lab_2.main import Command as Lab2Command
from lab_3.main import Command as Lab3Command
from lab_4.main import Command as Lab4Command
from lab_5.main import Command as Lab5Command
from lab_6.main import Command as Lab6Command
from lab_7.main import Command as Lab7Command
from lab_8.main import Command as Lab8Command

class Runner:
    def __init__(self):
        self.commands = {}
        self._initialize_commands()

    def _initialize_commands(self):
        try:
            self.commands["1"] = Lab1Command()
            self.commands["2"] = Lab2Command()
            self.commands["3"] = Lab3Command()
            self.commands["4"] = Lab4Command()
            self.commands["5"] = Lab5Command()
            self.commands["6"] = Lab6Command()
            self.commands["7"] = Lab7Command()
            self.commands["8"] = Lab8Command()
        except ImportError as e:
            print(f"Помилка при завантаженні команд: {e}")

    def display_menu(self):
        print("\nМеню запуску лабораторних робіт:")
        if not self.commands:
            print("Немає доступних лабораторних робіт")
            return
        
        for number in sorted(self.commands.keys()):
            print(f"Лабораторна робота №{number}")
        print("Введіть номер лабораторної роботи або 'q' для виходу")

    def start(self):
        print("Ласкаво просимо до системи виконання лабораторних робіт!")
        
        while True:
            try:
                self.display_menu()
                choice = input("Ваш вибір: ").strip().lower()
                
                if choice == 'q':
                    print("Дякуємо за використання програми!")
                    break
                
                if not choice:
                    print("Будь ласка, зробіть вибір")
                    continue

                command = self.commands.get(choice)
                if command:
                    command.execute()
                else:
                    print("Невірний номер лабораторної роботи")
                    
            except KeyboardInterrupt:
                print("\nПрограму завершено користувачем")
                break
            except Exception as e:
                print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    runner = Runner()
    runner.start()