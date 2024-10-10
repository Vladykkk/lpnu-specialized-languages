from bll.shape3d_operations import Shape3DOperations
from bll.ascii_art_generator import ASCIIArtGenerator
from dal.shapes import Cube, Pyramid, Sphere, Cylinder

class ASCII3DInterface:
    def __init__(self):
        self.generator = ASCIIArtGenerator()
        self.operations = Shape3DOperations()
        self.current_shape = None

    def create_shape(self):
        print("Choose a shape: 1. Cube, 2. Pyramid, 3. Sphere, 4. Cylinder")
        choice = input("Your choice: ")

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
            print("Create a shape first!")
        else:
            dx = float(input("Enter dx: "))
            dy = float(input("Enter dy: "))
            dz = float(input("Enter dz: "))
            self.operations.translate_shape(self.current_shape, dx, dy, dz)
            self.generator.draw_shape(self.current_shape)

    def display_shape(self):
        print(self.generator.render())
