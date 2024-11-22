class ASCIIArtService:
    def __init__(self, character_repository):
        self.char_set = character_repository.load_characters()

    def generate_art(self, text, width, height):
        ascii_lines = ['' for _ in range(height)]
        for char in text:
            char_lines = self.char_set.get(char, [' ' * width] * height)
            for i in range(height):
                ascii_lines[i] += char_lines[i] + ' '  # Add space between characters
        return ascii_lines

    def align_art(self, ascii_art, text_length, width, alignment):
        total_width = width * text_length
        aligned_art = []
        for line in ascii_art:
            if alignment == 'left':
                aligned_art.append(line.ljust(total_width))
            elif alignment == 'center':
                aligned_art.append(line.center(total_width))
            elif alignment == 'right':
                aligned_art.append(line.rjust(total_width))
        return aligned_art
