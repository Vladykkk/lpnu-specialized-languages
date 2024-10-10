from dal import CalculatorMemory, CalculatorHistory
from bll import Calculator
from sources import FileStorage

def main():
    calc = Calculator()
    memory = CalculatorMemory()
    history = CalculatorHistory()

    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")

            if operator not in ['+', '-', '*', '/', '^', '√', '%']:
                print("Недійсний оператор. Будь ласка, введіть один з +, -, *, /, ^, √, %")
                continue

            num2 = None
            if operator != '√':
                num2 = float(input("Введіть друге число: "))

            result = calc.perform_calculation(num1, num2, operator)
            formatted_result = calc.format_result(result)

            expression = f"{num1} {operator} {num2}" if num2 is not None else f"{operator}{num1}"
            print(f"Результат: {formatted_result}")
            history.add_to_history(expression, formatted_result)

            action = input("Виберіть дію (н - нове обчислення, і - історія, п - пам'ять, н - налаштування, з - зберегти в файл, в - вихід): ").lower()

            if action == 'о':
                continue
            elif action == 'і':
                for item in history.get_history():
                    print(item)
            elif action == 'п':
                mem_action = input("Зберегти (з) чи відновити (в) значення з пам'яті? ").lower()
                if mem_action == 'з':
                    memory.store_in_memory(result)
                    print("Значення збережено в пам'яті")
                elif mem_action == 'в':
                    print(f"Значення з пам'яті: {memory.recall_from_memory()}")
            elif action == 'н':
                new_places = int(input("Введіть кількість десяткових розрядів для відображення: "))
                calc.set_decimal_places(new_places)
                print(f"Кількість десяткових розрядів встановлено на {new_places}")
            elif action == 'з':
                FileStorage.save_history_to_file(history.get_history())
                print("Історію збережено у файл.")
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
