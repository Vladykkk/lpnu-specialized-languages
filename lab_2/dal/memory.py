class Memory:
    def __init__(self):
        self._memory = 0

    def store(self, value):
        self._memory = value

    def recall(self):
        return self._memory
