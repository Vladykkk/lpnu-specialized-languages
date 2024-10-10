def save_ascii_art_to_file(ascii_art: str, file_name: str):
    with open(file_name, 'w') as file:
        file.write(ascii_art)
