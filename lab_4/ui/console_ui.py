class ConsoleUI:
    @staticmethod
    def get_user_input():
        text = input("Введіть слово або фразу для перетворення в ASCII-арт: ")
        width = int(input("Введіть ширину для кожного символу (за замовчуванням 10): ") or 10)
        height = int(input("Введіть висоту для кожного символу (за замовчуванням 10): ") or 10)

        # Покращений UX для вирівнювання тексту
        print("Виберіть вирівнювання тексту:")
        print("1. Зліва")
        print("2. По центру")
        print("3. Справа")
        alignment_option = input("Виберіть опцію (1, 2 або 3): ").strip()
        
        alignment = 'left'
        if alignment_option == '2':
            alignment = 'center'
        elif alignment_option == '3':
            alignment = 'right'
        return text, width, height, alignment

    @staticmethod
    def display_art(ascii_art):
        for line in ascii_art:
            print(line)

    @staticmethod
    def save_art_option(ascii_art):
        print("Чи хочете ви зберегти ASCII-арт у файл?")
        print("1. Так")
        print("2. Ні")
        save_option = input("Виберіть опцію (1 або 2): ").strip()
        
        if save_option == '1':
            filename = input("Введіть ім'я файлу для збереження ASCII-арту (наприклад, art.txt): ")
            with open(filename, 'w') as file:
                for line in ascii_art:
                    file.write(line + '\n')
            print(f"ASCII-арт збережено у {filename}")
        elif save_option == '2':
            print("ASCII-арт не збережено.")
        else:
            print("Невірна опція. ASCII-арт не збережено.")
