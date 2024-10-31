import pyfiglet
from termcolor import colored

def generate_ascii_art(text, font='standard', color='white', width=0, symbols=''):
    if width > 0:
        ascii_art = pyfiglet.figlet_format(text, font=font, width=width)
    else:
        ascii_art = pyfiglet.figlet_format(text, font=font)
    
    if symbols:
        ascii_art = replace_symbols(ascii_art, symbols)
    
    colored_ascii_art = colored(ascii_art, color)
    return colored_ascii_art

def replace_symbols(ascii_art, symbols):
    symbol_map = {' ': symbols[0] if len(symbols) > 0 else ' ',
                  '_': symbols[1] if len(symbols) > 1 else '_',
                  '|': symbols[2] if len(symbols) > 2 else '|',
                  '/': symbols[3] if len(symbols) > 3 else '/',
                  '\\': symbols[4] if len(symbols) > 4 else '\\'}
    
    return ''.join(symbol_map.get(char, char) for char in ascii_art)

def save_ascii_art(ascii_art, filename):
    with open(filename, 'w') as file:
        file.write(ascii_art)