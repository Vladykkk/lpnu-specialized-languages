from ui.ascii3d_interface import ASCII3DInterface
from sources.file_operations import save_ascii_art_to_file

def main():
    interface = ASCII3DInterface()
    
    while True:
        print("\n1. Create Shape\n2. Manipulate Shape\n3. Display Shape\n4. Save ASCII Art\n5. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            interface.create_shape()
        elif choice == "2":
            interface.manipulate_shape()
        elif choice == "3":
            interface.display_shape()
        elif choice == "4":
            ascii_art = interface.generator.render()
            file_name = input("Enter file name to save: ")
            save_ascii_art_to_file(ascii_art, file_name)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
