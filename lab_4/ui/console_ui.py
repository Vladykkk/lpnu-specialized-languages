class ConsoleUI:
    @staticmethod
    def get_user_input():
        text = input("Enter the word or phrase to convert into ASCII art: ")
        width = int(input("Enter the width for each character (default is 10): ") or 10)
        height = int(input("Enter the height for each character (default is 10): ") or 10)

        # Improved UX for text alignment
        print("Choose text alignment:")
        print("1. Left")
        print("2. Center")
        print("3. Right")
        alignment_option = input("Choose an option (1, 2, or 3): ").strip()
        
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
        print("Do you want to save the ASCII art to a file?")
        print("1. Yes")
        print("2. No")
        save_option = input("Choose an option (1 or 2): ").strip()
        
        if save_option == '1':
            filename = input("Enter the filename to save the ASCII art (e.g., art.txt): ")
            with open(filename, 'w') as file:
                for line in ascii_art:
                    file.write(line + '\n')
            print(f"ASCII art saved to {filename}")
        elif save_option == '2':
            print("ASCII art not saved.")
        else:
            print("Invalid option. ASCII art not saved.")
