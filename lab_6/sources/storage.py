class FileStorage:
    @staticmethod
    def save_history_to_file(history, filename="history.txt"):
        with open(filename, "w") as file:
            for item in history:
                file.write(f"{item}\n")

    @staticmethod
    def load_history_from_file(filename="history.txt"):
        try:
            with open(filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []
