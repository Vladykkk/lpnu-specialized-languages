from user_interface import UserInterface
from ascii_generator import ASCIIGenerator
from file_handler import FileHandler

def main():
    ui = UserInterface()
    generator = ASCIIGenerator()
    file_handler = FileHandler()

    while True:
        choice = ui.main_menu()
        if choice == '1':
            text = ui.get_text()
            width, height = ui.get_dimensions()
            alignment = ui.get_alignment()
            color_option = ui.get_color_option()
            
            ascii_art = generator.generate_art(text, width, height, alignment, color_option)
            ui.display_preview(ascii_art)
            
            if ui.confirm_save():
                filename = ui.get_filename()
                file_handler.save_to_file(ascii_art, filename)
                print(f"ASCII art saved to {filename}")
        elif choice == '2':
            break

if __name__ == "__main__":
    main()