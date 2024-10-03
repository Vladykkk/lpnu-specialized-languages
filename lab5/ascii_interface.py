from ascii_art_generator import ASCIIArtGenerator
from shape import Cube, Pyramid, Sphere, Cylinder
from colorama import Fore

class ASCII3DInterface:
    def init(self):
        self.generator = ASCIIArtGenerator()
        self.current_shape = None

    def create_shape(self):
        print("Виберіть фігуру для створення:")
        print("1. Куб")
        print("2. Піраміда")
        print("3. Сфера")
        print("4. Циліндр")
        choice = input("Ваш вибір (1-4): ")

        color_choice = input("Виберіть колір (r/g/b/w): ").lower()
        color_map = {
            'r': Fore.RED,
            'g': Fore.GREEN,
            'b': Fore.BLUE,
            'w': Fore.WHITE
        }
        color = color_map.get(color_choice, Fore.WHITE)

        if choice == "1":
            size = float(input("Введіть розмір куба (1.0): ") or 1.0)
            self.current_shape = Cube(size, color)
        elif choice == "2":
            base = float(input("Введіть розмір основи піраміди (1.0): ") or 1.0)
            height = float(input("Введіть висоту піраміди (1.5): ") or 1.5)
            self.current_shape = Pyramid(base, height, color)
        elif choice == "3":
            radius = float(input("Введіть радіус сфери (1.0): ") or 1.0)
            segments = int(input("Введіть кількість сегментів (8): ") or 8)
            self.current_shape = Sphere(radius, segments, color)
        elif choice == "4":
            radius = float(input("Введіть радіус циліндра (1.0): ") or 1.0)
            height = float(input("Введіть висоту циліндра (2.0): ") or 2.0)
            segments = int(input("Введіть кількість сегментів (8): ") or 8)
            self.current_shape = Cylinder(radius, height, segments, color)

    def manipulate_shape(self):
        # Code for manipulating shapes...
