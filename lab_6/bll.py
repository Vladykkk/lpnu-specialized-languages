import math

class Calculator:
    def __init__(self, decimal_places=2):
        self.decimal_places = decimal_places

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

    def set_decimal_places(self, places):
        self.decimal_places = places

    def format_result(self, result):
        return round(result, self.decimal_places)
