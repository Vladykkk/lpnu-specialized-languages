from bll.shape3d_operations import Shape3DOperations
from bll.ascii_art_generator import ASCIIArtGenerator
from dal.shapes import Cube, Pyramid, Sphere, Cylinder

class ConsoleUI:
    def __init__(self):
        self.generator = ASCIIArtGenerator()
        self.operations = Shape3DOperations()
        self.current_shape = None

    def create_shape(self):
        print("Оберіть фігуру: 1. Куб, 2. Піраміда, 3. Сфера, 4. Циліндр")
        choice = input("Ваш вибір: ")

        if choice == "1":
            self.current_shape = Cube()
        elif choice == "2":
            self.current_shape = Pyramid()
        elif choice == "3":
            self.current_shape = Sphere()
        elif choice == "4":
            self.current_shape = Cylinder()

    def manipulate_shape(self):
        if not self.current_shape:
            print("Спочатку створіть фігуру!")
        else:
            dx = float(input("Введіть dx: "))
            dy = float(input("Введіть dy: "))
            dz = float(input("Введіть dz: "))
            self.operations.translate_shape(self.current_shape, dx, dy, dz)
            self.generator.draw_shape(self.current_shape)

    def display_shape(self):
        print(self.generator.render())
