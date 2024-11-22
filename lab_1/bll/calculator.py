import math

def perform_calculation(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                raise ValueError("Ділення на нуль неможливе")
            return num1 / num2
        case '^':
            return num1 ** num2
        case '√':
            if num1 < 0:
                raise ValueError("Неможливо обчислити квадратний корінь від від'ємного числа")
            return math.sqrt(num1)
        case '%':
            return num1 % num2
        case _:
            raise ValueError("Невідомий оператор")

def add_to_history(history, expression, result):
    history.append(f"{expression} = {result}")

def show_history(history):
    return history

def set_decimal_places(current_places, new_places):
    return new_places
