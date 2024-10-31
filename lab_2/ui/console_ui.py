from bll.calculator import Calculator

class ConsoleUI:
    def __init__(self):
        self.calc = Calculator()

    def run(self):
        while True:
            try:
                num1 = float(input("Введіть перше число: "))
                operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
                
                if operator not in ['+', '-', '*', '/', '^', '√', '%']:
                    print("Недійсний оператор. Будь ласка, введіть один з +, -, *, /, ^, √, %")
                    continue

                num2 = float(input("Введіть друге число: ")) if operator != '√' else None

                result = self.calc.perform_calculation(num1, num2, operator)
                expression = f"{num1} {operator} {num2}" if num2 is not None else f"{operator}{num1}"
                formatted_result = round(result, self.calc.decimal_places)

                print(f"Результат: {formatted_result}")
                self.calc.add_to_history(expression, formatted_result)

                self.handle_action(result)

            except ValueError as e:
                print(f"Помилка: {str(e)}")
            except Exception as e:
                print(f"Виникла непередбачена помилка: {str(e)}")

    def handle_action(self, result):
        action = input("Виберіть дію (н - нове обчислення, і - історія, п - пам'ять, н - налаштування, в - вихід): ").lower()
        
        match action:
            case 'н':
                pass
            case 'і':
                for item in self.calc.show_history():
                    print(item)
            case 'п':
                mem_action = input("Зберегти (з) чи відновити (в) значення з пам'яті? ").lower()
                if mem_action == 'з':
                    self.calc.memory.store(result)
                    print("Значення збережено в пам'яті")
                elif mem_action == 'в':
                    print(f"Значення з пам'яті: {self.calc.memory.recall()}")
            case 'н':
                new_places = int(input("Введіть кількість десяткових розрядів для відображення: "))
                self.calc.set_decimal_places(new_places)
                print(f"Кількість десяткових розрядів встановлено на {new_places}")
            case 'в':
                print("Дякуємо за використання калькулятора!")
                exit()
            case _:
                print("Невідома дія. Продовжуємо...")
