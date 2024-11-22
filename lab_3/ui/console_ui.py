from ascii_art.art_generator import generate_ascii_art, save_ascii_art
from ascii_art.fonts import get_available_fonts
from ascii_art.colors import get_available_colors

class ConsoleUI:
    def __init__(self):
        self.ascii_art = None

    def print_menu(self):
        print("\n--- ASCII Art Generator ---")
        print("1. Створити новий ASCII-арт")
        print("2. Вийти")

    def get_user_choice(self, prompt, options):
        while True:
            choice = input(prompt)
            if choice in options:
                return choice
            print("Невірний вибір. Спробуйте ще раз.")

    def create_ascii_art(self):
        user_input = input("Введіть слово або фразу для перетворення в ASCII-арт: ")

        available_fonts = get_available_fonts()
        print("Доступні шрифти:", ', '.join(available_fonts))
        font_choice = self.get_user_choice("Виберіть шрифт з доступних: ", available_fonts)

        available_colors = get_available_colors()
        print("Доступні кольори:", ', '.join(available_colors))
        color_choice = self.get_user_choice("Виберіть колір з доступних: ", available_colors)

        width = int(input("Введіть бажану ширину ASCII-арту (або 0 для автоматичного розміру): "))

        symbols = input("Введіть символи для створення ASCII-арту (залиште порожнім для стандартних): ")

        self.ascii_art = generate_ascii_art(user_input, font=font_choice, color=color_choice, width=width, symbols=symbols)

        self.preview_ascii_art()
        self.save_ascii_art_option()

    def preview_ascii_art(self):
        preview_choice = self.get_user_choice("Бажаєте переглянути попередній перегляд ASCII-арту? (так/ні): ", ['так', 'ні'])
        if preview_choice.lower() == 'так' and self.ascii_art:
            print(self.ascii_art)

    def save_ascii_art_option(self):
        save_choice = self.get_user_choice("Бажаєте зберегти ASCII-арт у файл? (так/ні): ", ['так', 'ні'])
        if save_choice.lower() == 'так' and self.ascii_art:
            filename = input("Введіть ім'я файлу для збереження: ")
            save_ascii_art(self.ascii_art, filename)
            print(f"ASCII-арт збережено у файл {filename}")

    def run(self):
        while True:
            self.print_menu()
            choice = self.get_user_choice("Виберіть опцію (1-2): ", ['1', '2'])

            if choice == '2':
                print("Дякуємо за використання ASCII Art Generator!")
                break
            elif choice == '1':
                self.create_ascii_art()
