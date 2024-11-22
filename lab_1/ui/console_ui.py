from lab_1.bll.calculator import perform_calculation, add_to_history, show_history, set_decimal_places
from lab_1.dal.memory import store_memory, recall_memory

decimal_places = 2
history = []
memory = 0

def run_console_ui():
    global decimal_places, history, memory

    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")

            if operator not in ['+', '-', '*', '/', '^', '√', '%']:
                print("Недійсний оператор. Будь ласка, введіть один з +, -, *, /, ^, √, %")
                continue

            num2 = float(input("Введіть друге число: ")) if operator != '√' else None
            result = perform_calculation(num1, num2, operator)

            expression = f"{num1} {operator} {num2}" if num2 is not None else f"{operator}{num1}"
            formatted_result = round(result, decimal_places)

            print(f"Результат: {formatted_result}")
            add_to_history(history, expression, formatted_result)

            handle_action(result)
        except ValueError as e:
            print(f"Помилка: {str(e)}")
        except Exception as e:
            print(f"Виникла непередбачена помилка: {str(e)}")

def handle_action(result):
    global decimal_places, history, memory

    action = input("Виберіть дію (н - нове обчислення, і - історія, п - пам'ять, н - налаштування, в - вихід): ").lower()
    
    match action:
        case 'н':
            pass
        case 'і':
            for item in show_history(history):
                print(item)
        case 'п':
            mem_action = input("Зберегти (з) чи відновити (в) значення з пам'яті? ").lower()
            if mem_action == 'з':
                memory = store_memory(memory, result)
                print("Значення збережено в пам'яті")
            elif mem_action == 'в':
                print(f"Значення з пам'яті: {recall_memory(memory)}")
        case 'н':
            new_places = int(input("Введіть кількість десяткових розрядів для відображення: "))
            decimal_places = set_decimal_places(decimal_places, new_places)
            print(f"Кількість десяткових розрядів встановлено на {decimal_places}")
        case 'в':
            print("Дякуємо за використання калькулятора!")
            exit()
        case _:
            print("Невідома дія. Продовжуємо...")
