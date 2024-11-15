from ..dal.memory import CalculatorMemory, CalculatorHistory
from ..bll.operations import Calculator
from ..sources.storage import FileStorage

class ConsoleUI:
    def __init__(self):
        self.calc = Calculator()
        self.memory = CalculatorMemory()
        self.history = CalculatorHistory()

    def run(self):
        while True:
            try:
                if not self._perform_calculation():
                    break
            except ValueError as e:
                print(f"Помилка: {str(e)}")
            except Exception as e:
                print(f"Виникла непередбачена помилка: {str(e)}")

    def _perform_calculation(self):
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")

        if operator not in ['+', '-', '*', '/', '^', '√', '%']:
            print("Недійсний оператор. Будь ласка, введіть один з +, -, *, /, ^, √, %")
            return True

        num2 = None
        if operator != '√':
            num2 = float(input("Введіть друге число: "))

        result = self.calc.perform_calculation(num1, num2, operator)
        formatted_result = self.calc.format_result(result)

        expression = f"{num1} {operator} {num2}" if num2 is not None else f"{operator}{num1}"
        print(f"Результат: {formatted_result}")
        self.history.add_to_history(expression, formatted_result)

        return self._handle_action(result)

    def _handle_action(self, result):
        action = input("Виберіть дію (н - нове обчислення, і - історія, п - пам'ять, н - налаштування, з - зберегти в файл, в - вихід): ").lower()

        actions = {
            'н': lambda: True,
            'і': self._show_history,
            'п': lambda: self._handle_memory(result),
            'н': self._change_settings,
            'з': self._save_to_file,
            'в': self._exit
        }

        if action in actions:
            return actions[action]()
        else:
            print("Невідома дія. Продовжуємо...")
            return True

    def _show_history(self):
        for item in self.history.get_history():
            print(item)
        return True

    def _handle_memory(self, result):
        mem_action = input("Зберегти (з) чи відновити (в) значення з пам'яті? ").lower()
        if mem_action == 'з':
            self.memory.store_in_memory(result)
            print("Значення збережено в пам'яті")
        elif mem_action == 'в':
            print(f"Значення з пам'яті: {self.memory.recall_from_memory()}")
        return True

    def _change_settings(self):
        try:
            new_places = int(input("Введіть кількість десяткових розрядів для відображення: "))
            self.calc.set_decimal_places(new_places)
            print(f"Кількість десяткових розрядів встановлено на {new_places}")
        except ValueError:
            print("Введіть коректне число")
        return True

    def _save_to_file(self):
        FileStorage.save_history_to_file(self.history.get_history())
        print("Історію збережено у файл.")
        return True

    def _exit(self):
        print("Дякуємо за використання калькулятора!")
        return False