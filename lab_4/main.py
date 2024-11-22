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
        # Load ASCII art from text files for letters, numbers, and symbols
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;':\",.<>?/ ":
            if char.isalpha():
                filename = f"alphabets/{char}.txt"
            elif char.isdigit():
                filename = f"numbers/{char}.txt"
            else:
                filename = f"symbols/{char}.txt"
                
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    self.char_set[char] = [line.rstrip('\n') for line in file.readlines()]
            else:
                self.char_set[char] = [' ' * 10] * 10  # Default to blank if file doesn't exist

    # Task 1: User Input
    def get_user_input(self):
        self.text = input("Enter the word or phrase to convert into ASCII art: ")
        self.width = int(input("Enter the width for each character (default is 10): ") or 10)
        self.height = int(input("Enter the height for each character (default is 10): ") or 10)

        # Improved UX for text alignment
        print("Choose text alignment:")
        print("1. Left")
        print("2. Center")
        print("3. Right")
        alignment_option = input("Choose an option (1, 2, or 3): ").strip()
        
        if alignment_option == '1':
            self.alignment = 'left'
        elif alignment_option == '2':
            self.alignment = 'center'
        elif alignment_option == '3':
            self.alignment = 'right'
        else:
            print("Invalid option. Defaulting to left alignment.")
            self.alignment = 'left'

    # Task 2-5: Generate ASCII Art
    def generate_art(self):
        ascii_lines = ['' for _ in range(self.height)]
        for char in self.text:
            if char in self.char_set:
                char_lines = self.char_set[char]
            else:
                # Handle undefined characters by using a blank space
                char_lines = [' ' * self.width] * self.height
            
            # Ensure char_lines has enough lines
            if len(char_lines) < self.height:
                char_lines += [' ' * self.width] * (self.height - len(char_lines))
                
            for i in range(self.height):
                ascii_lines[i] += char_lines[i] + ' '  # Add a single space between characters
        return ascii_lines

    # Task 6: Display Art
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

    # New Method: Save Art to File
    def save_art_to_file(self, ascii_art):
        filename = input("Enter the filename to save the ASCII art (e.g., art.txt): ")
        with open(filename, 'w') as file:
            for line in ascii_art:
                file.write(line + '\n')
        print(f"ASCII art saved to {filename}")

# Task 10: User Interface
class Lab4Command:
    def execute(self):
        generator = ASCIIGenerator()
        generator.get_user_input()
        
        ascii_art = generator.generate_art()
        
        # Display Art
        generator.display_art(ascii_art)

        # Save Art
        print("Do you want to save the ASCII art to a file?")
        print("1. Yes")
        print("2. No")
        save_option = input("Choose an option (1 or 2): ").strip()
        
        if save_option == '1':
            generator.save_art_to_file(ascii_art)
        elif save_option == '2':
            print("ASCII art not saved.")
        else:
            print("Invalid option. ASCII art not saved.")