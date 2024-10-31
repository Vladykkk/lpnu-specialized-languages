from ascii_art.art_generator import generate_ascii_art, save_ascii_art
from ascii_art.fonts import get_available_fonts
from ascii_art.colors import get_available_colors

def print_menu():
    print("\n--- ASCII Art Generator ---")
    print("1. Створити новий ASCII-арт")
    print("2. Вийти")

def get_user_choice(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        print("Невірний вибір. Спробуйте ще раз.")

def main():
    while True:
        print_menu()
        choice = get_user_choice("Виберіть опцію (1-2): ", ['1', '2'])
        
        if choice == '2':
            print("Дякуємо за використання ASCII Art Generator!")
            break
        
        user_input = input("Введіть слово або фразу для перетворення в ASCII-арт: ")
        
        available_fonts = get_available_fonts()
        print("Доступні шрифти:", ', '.join(available_fonts))
        font_choice = get_user_choice("Виберіть шрифт з доступних: ", available_fonts)
        
        available_colors = get_available_colors()
        print("Доступні кольори:", ', '.join(available_colors))
        color_choice = get_user_choice("Виберіть колір з доступних: ", available_colors)
        
        width = int(input("Введіть бажану ширину ASCII-арту (або 0 для автоматичного розміру): "))
        
        symbols = input("Введіть символи для створення ASCII-арту (залиште порожнім для стандартних): ")
        
        ascii_art = generate_ascii_art(user_input, font=font_choice, color=color_choice, width=width, symbols=symbols)
        
        preview_choice = get_user_choice("Бажаєте переглянути попередній перегляд ASCII-арту? (так/ні): ", ['так', 'ні'])
        if preview_choice.lower() == 'так':
            print(ascii_art)
        
        save_choice = get_user_choice("Бажаєте зберегти ASCII-арт у файл? (так/ні): ", ['так', 'ні'])
        if save_choice.lower() == 'так':
            filename = input("Введіть ім'я файлу для збереження: ")
            save_ascii_art(ascii_art, filename)
            print(f"ASCII-арт збережено у файл {filename}")

if __name__ == "__main__":
    main()