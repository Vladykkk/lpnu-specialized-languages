import math

class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []
        self.decimal_places = 2

    def perform_calculation(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("Ділення на нуль неможливе")
            return num1 / num2
        elif operator == '^':
            return num1 ** num2
        elif operator == '√':
            if num1 < 0:
                raise ValueError("Неможливо обчислити квадратний корінь від від'ємного числа")
            return math.sqrt(num1)
        elif operator == '%':
            return num1 % num2
        else:
            raise ValueError("Невідомий оператор")

    def store_in_memory(self, value):
        self.memory = value

    def recall_from_memory(self):
        return self.memory

    def add_to_history(self, expression, result):
        self.history.append(f"{expression} = {result}")

    def show_history(self):
        for item in self.history:
            print(item)

    def set_decimal_places(self, places):
        self.decimal_places = places

def main():
    calc = Calculator()

    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            
            if operator not in ['+', '-', '*', '/', '^', '√', '%']:
                print("Недійсний оператор. Будь ласка, введіть один з +, -, *, /, ^, √, %")
                continue

            if operator != '√':
                num2 = float(input("Введіть друге число: "))
            else:
                num2 = None

            result = calc.perform_calculation(num1, num2, operator)
            
            expression = f"{num1} {operator} {num2}" if num2 is not None else f"{operator}{num1}"
            formatted_result = round(result, calc.decimal_places)
            
            print(f"Результат: {formatted_result}")
            
            calc.add_to_history(expression, formatted_result)

            action = input("Виберіть дію (н - нове обчислення, і - історія, п - пам'ять, н - налаштування, в - вихід): ").lower()
            
            if action == 'н':
                continue
            elif action == 'і':
                calc.show_history()
            elif action == 'п':
                mem_action = input("Зберегти (з) чи відновити (в) значення з пам'яті? ").lower()
                if mem_action == 'з':
                    calc.store_in_memory(result)
                    print("Значення збережено в пам'яті")
                elif mem_action == 'в':
                    print(f"Значення з пам'яті: {calc.recall_from_memory()}")
            elif action == 'н':
                new_places = int(input("Введіть кількість десяткових розрядів для відображення: "))
                calc.set_decimal_places(new_places)
                print(f"Кількість десяткових розрядів встановлено на {new_places}")
            elif action == 'в':
                print("Дякуємо за використання калькулятора!")
                break
            else:
                print("Невідома дія. Продовжуємо...")

        except ValueError as e:
            print(f"Помилка: {str(e)}")
        except Exception as e:
            print(f"Виникла непередбачена помилка: {str(e)}")

if __name__ == "__main__":
    main()