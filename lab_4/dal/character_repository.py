import os

class CharacterRepository:
    @staticmethod
    def load_characters(width=10, height=10):
        char_set = {}
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;':\",.<>?/ ":
            if char.isalpha():
                filename = f"alphabets/{char}.txt"
            elif char.isdigit():
                filename = f"numbers/{char}.txt"
            else:
                filename = f"symbols/{char}.txt"
                
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    char_lines = [line.rstrip('\n') for line in file.readlines()]
                    char_lines = char_lines[:height] + [' ' * width] * (height - len(char_lines))  # Adjust height
                    char_set[char] = char_lines
            else:
                char_set[char] = [' ' * width] * height
        return char_set
