import os

class FileHandler:
    def save_to_file(self, ascii_art, filename):
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as file:
            file.write(ascii_art)