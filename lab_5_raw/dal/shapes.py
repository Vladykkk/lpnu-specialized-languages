from typing import List
from colorama import Fore
from .point3d import Point3D

class Shape3D:
    def __init__(self, points: List[Point3D], color: str = Fore.WHITE):
        self.points = points
        self.color = color
        self.position = Point3D(0, 0, 0)
        self.scale = 1.0

    def translate(self, dx: float, dy: float, dz: float):
        self.position.x += dx
        self.position.y += dy
        self.position.z += dz

    def scale_shape(self, factor: float):
        self.scale *= factor


class Cube(Shape3D):
    def __init__(self, size: float = 1.0, color: str = Fore.WHITE):
        points = [
            Point3D(-size/2, -size/2, -size/2),
            Point3D(size/2, -size/2, -size/2),
            Point3D(size/2, size/2, -size/2),
            Point3D(-size/2, size/2, -size/2),
            Point3D(-size/2, -size/2, size/2),
            Point3D(size/2, -size/2, size/2),
            Point3D(size/2, size/2, size/2),
            Point3D(-size/2, size/2, size/2)
        ]
        super().__init__(points, color)


class Pyramid(Shape3D):
    def __init__(self, base_size: float = 1.0, height: float = 1.5, color: str = Fore.WHITE):
        points = [
            Point3D(-base_size/2, 0, -base_size/2),
            Point3D(base_size/2, 0, -base_size/2),
            Point3D(base_size/2, 0, base_size/2),
            Point3D(-base_size/2, 0, base_size/2),
            Point3D(0, height, 0)
        ]
        super().__init__(points, color)


class Sphere(Shape3D):
    def __init__(self, radius: float = 1.0, segments: int = 8, color: str = Fore.WHITE):
        points = []
        for i in range(segments):
            phi = (i * math.pi) / (segments - 1)
            for j in range(segments * 2):
                theta = (j * 2 * math.pi) / (segments * 2)
                x = radius * math.sin(phi) * math.cos(theta)
                y = radius * math.cos(phi)
                z = radius * math.sin(phi) * math.sin(theta)
                points.append(Point3D(x, y, z))
        super().__init__(points, color)


class Cylinder(Shape3D):
    def __init__(self, radius: float = 1.0, height: float = 2.0, segments: int = 8, color: str = Fore.WHITE):
        points = []
        for i in range(segments):
            angle = (i * 2 * math.pi) / segments
            x = radius * math.cos(angle)
            z = radius * math.sin(angle)
            points.append(Point3D(x, height/2, z))
        
        for i in range(segments):
            angle = (i * 2 * math.pi) / segments
            x = radius * math.cos(angle)
            z = radius * math.sin(angle)
            points.append(Point3D(x, -height/2, z))
        
        super().__init__(points, color)
