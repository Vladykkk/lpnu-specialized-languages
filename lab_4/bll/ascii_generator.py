import os

class ASCIIGenerator:
    def __init__(self):
        self.char_set = {}
        self.load_characters()
        self.width = 0
        self.height = 0
        self.text = ""
        self.alignment = "left"

    def load_characters(self):
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;':\",.<>?/ ":
            if char.isalpha():
                filename = f"lab_4/alphabets/{char}.txt"
            elif char.isdigit():
                filename = f"lab_4/numbers/{char}.txt"
            else:
                filename = f"lab_4/symbols/{char}.txt"
                
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    self.char_set[char] = [line.rstrip('\n') for line in file.readlines()]
            else:
                self.char_set[char] = [' ' * 10] * 10  # Default to blank if file doesn't exist

    def get_user_input(self):
        self.text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")
        self.width = int(input("Введіть ширину для кожного символу (за замовчуванням 10): ") or 10)
        self.height = int(input("Введіть висоту для кожного символу (за замовчуванням 10): ") or 10)

        # Покращений UX для вирівнювання тексту
        print("Оберіть вирівнювання тексту:")
        print("1. Зліва")
        print("2. По центру")
        print("3. Справа")
        alignment_option = input("Оберіть опцію (1, 2 або 3): ").strip()
        
        if alignment_option == '1':
            self.alignment = 'left'
        elif alignment_option == '2':
            self.alignment = 'center'
        elif alignment_option == '3':
            self.alignment = 'right'
        else:
            print("Невірний вибір. За замовчуванням використано вирівнювання зліва.")
            self.alignment = 'left'

    # Завдання 2-5: Генерація ASCII-арту
    def generate_art(self):
        ascii_lines = ['' for _ in range(self.height)]
        for char in self.text:
            if char in self.char_set:
                char_lines = self.char_set[char]
            else:
                # Обробка невизначених символів за допомогою порожнього простору
                char_lines = [' ' * self.width] * self.height
            
            # Перевірка, чи є достатньо рядків у char_lines
            if len(char_lines) < self.height:
                char_lines += [' ' * self.width] * (self.height - len(char_lines))
                
            for i in range(self.height):
                ascii_lines[i] += char_lines[i] + ' '  # Додаємо один пробіл між символами
        return ascii_lines

    # Завдання 6: Виведення арту
    def display_art(self, ascii_art):
        for line in ascii_art:
            aligned_line = self._align_line(line, self.width * len(self.text))
            print(aligned_line)

    def _align_line(self, line, width):
        if self.alignment == 'left':
            return line.ljust(width)
        elif self.alignment == 'center':
            return line.center(width)
        elif self.alignment == 'right':
            return line.rjust(width)
        else:
            return line

    # Новий метод: Зберегти арт у файл
    def save_art_to_file(self, ascii_art):
        filename = input("Введіть ім'я файлу для збереження ASCII-арту (наприклад, art.txt): ")
        with open(filename, 'w') as file:
            for line in ascii_art:
                file.write(line + '\n')
        print(f"ASCII-арт збережено в {filename}")
