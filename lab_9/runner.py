import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lab_2.command import Lab2Command
from lab_6.command import Lab6Command

class Runner:
    def __init__(self):
        self.commands = {}
        self._initialize_commands()

    def _initialize_commands(self):
        """Ініціалізація доступних команд"""
        try:
            self.commands["2"] = Lab2Command()
            self.commands["6"] = Lab6Command()
        except ImportError as e:
            print(f"Помилка при завантаженні команд: {e}")

    def display_menu(self):
        """Відображення меню вибору лабораторних робіт"""
        print("\nМеню запуску лабораторних робіт:")
        if not self.commands:
            print("Немає доступних лабораторних робіт")
            return
        
        for number in sorted(self.commands.keys()):
            print(f"Лабораторна робота №{number}")
        print("Введіть номер лабораторної роботи або 'q' для виходу")

    def start(self):
        """Головний цикл виконання програми"""
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