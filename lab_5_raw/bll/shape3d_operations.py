from dal.shapes import Shape3D, Cube, Pyramid, Sphere, Cylinder
from dal.point3d import Point3D

class Shape3DOperations:
    def translate_shape(self, shape: Shape3D, dx: float, dy: float, dz: float):
        shape.translate(dx, dy, dz)

    def scale_shape(self, shape: Shape3D, factor: float):
        shape.scale_shape(factor)
