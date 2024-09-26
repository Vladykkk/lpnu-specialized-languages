class UserInterface:
    def main_menu(self):
        print("\nASCII Art Generator")
        print("1. Create ASCII Art")
        print("2. Exit")
        return input("Choose an option: ")

    def get_text(self):
        return input("Enter text for ASCII art: ")

    def get_dimensions(self):
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        return width, height

    def get_alignment(self):
        print("Choose alignment:")
        print("1. Left")
        print("2. Center")
        print("3. Right")
        choice = input("Enter choice (1-3): ")
        alignments = ['left', 'center', 'right']
        return alignments[int(choice) - 1]

    def get_color_option(self):
        print("Choose color option:")
        print("1. Black and White")
        print("2. Grayscale")
        choice = input("Enter choice (1-2): ")
        return "bw" if choice == "1" else "grayscale"

    def display_preview(self, ascii_art):
        print("\nPreview:")
        print(ascii_art)

    def confirm_save(self):
        return input("Save this ASCII art? (y/n): ").lower() == 'y'

    def get_filename(self):
        return input("Enter filename to save: ")