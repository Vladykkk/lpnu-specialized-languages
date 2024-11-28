from lab_5.ui.console_ui import ConsoleUI
from sources.file_operations import save_ascii_art_to_file

class Command:
    def execute(self):
        interface = ConsoleUI()
        
        while True:
            print("\n1. Створити фігуру\n2. Змінити фігуру\n3. Відобразити фігуру\n4. Зберегти ASCII-графіку\n5. Вийти")
            choice = input("Ваш вибір: ")

            if choice == "1":
                interface.create_shape()
            elif choice == "2":
                interface.manipulate_shape()
            elif choice == "3":
                interface.display_shape()
            elif choice == "4":
                ascii_art = interface.generator.render()
                file_name = input("Введіть ім'я файлу для збереження: ")
                save_ascii_art_to_file(ascii_art, file_name)
            elif choice == "5":
                break
