class CalculatorMemory:
    def __init__(self):
        self.memory = 0

    def store_in_memory(self, value):
        self.memory = value

    def recall_from_memory(self):
        return self.memory

class CalculatorHistory:
    def __init__(self):
        self.history = []

    def add_to_history(self, expression, result):
        self.history.append(f"{expression} = {result}")

    def get_history(self):
        return self.history
