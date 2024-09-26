class ASCIIGenerator:
    def __init__(self):
        self.char_set = ' .:-=+*#%@'  # From least to most dense

    def generate_art(self, text, width, height, alignment, color_option):
        # Split the text into lines that fit within the width
        lines = self._split_text(text, width)
        
        # Pad or truncate lines to match the desired height
        lines = self._adjust_height(lines, height)
        
        # Apply alignment to each line
        aligned_lines = [self._align_line(line, width, alignment) for line in lines]
        
        # Convert text to ASCII art
        ascii_art = self._text_to_ascii(aligned_lines)
        
        return self._apply_color(ascii_art, color_option)

    def _split_text(self, text, max_width):
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + len(current_line) <= max_width:
                current_line.append(word)
                current_length += len(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)

        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def _adjust_height(self, lines, desired_height):
        current_height = len(lines)
        if current_height < desired_height:
            padding = (desired_height - current_height) // 2
            return [''] * padding + lines + [''] * (desired_height - current_height - padding)
        else:
            return lines[:desired_height]

    def _align_line(self, line, width, alignment):
        if alignment == 'left':
            return line.ljust(width)
        elif alignment == 'center':
            return line.center(width)
        else:  # right alignment
            return line.rjust(width)

    def _text_to_ascii(self, lines):
        ascii_art = []
        for line in lines:
            ascii_line = ''
            for char in line:
                if char.isalnum():
                    index = ord(char.lower()) - ord('a')
                    ascii_char = self.char_set[index % len(self.char_set)]
                elif char.isspace():
                    ascii_char = ' '
                else:
                    ascii_char = char
                ascii_line += ascii_char
            ascii_art.append(ascii_line)
        return '\n'.join(ascii_art)

    def _apply_color(self, ascii_art, color_option):
        if color_option == "bw":
            return ascii_art
        elif color_option == "grayscale":
            colored_art = ""
            for char in ascii_art:
                if char == ' ':
                    colored_art += char
                elif char == '\n':
                    colored_art += '\n'
                else:
                    gray_value = 232 + min(23, self.char_set.index(char) * 2)
                    colored_art += f"\033[38;5;{gray_value}m{char}\033[0m"
            return colored_art