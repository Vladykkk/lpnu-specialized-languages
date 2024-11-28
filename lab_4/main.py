from bll.ascii_generator import ASCIIGenerator

class Command:
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