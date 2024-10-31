import math
from dal.memory import Memory

class Calculator:
    def __init__(self):
        self.memory = Memory()
        self.history = []
        self.decimal_places = 2

    def perform_calculation(self, num1, num2, operator):
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

    def add_to_history(self, expression, result):
        self.history.append(f"{expression} = {result}")

    def show_history(self):
        return self.history

    def set_decimal_places(self, places):
        self.decimal_places = places
