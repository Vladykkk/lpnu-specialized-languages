from colorama import Fore, Style, init
from dal.point3d import Point3D
from dal.shapes import Shape3D
from typing import Optional, Tuple

class ASCIIArtGenerator:
    def __init__(self, width: int = 40, height: int = 20):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
        self.colors = [[Fore.WHITE for _ in range(width)] for _ in range(height)]
        init(autoreset=True)
        
    def project_point(self, point: Point3D) -> Optional[Tuple[int, int, float]]:
        z = point.z + 5
        if z <= 0:
            return None
        
        x = int(self.width/2 + (point.x * 100/z))
        y = int(self.height/2 + (point.y * 50/z))
        
        if 0 <= x < self.width and 0 <= y < self.height:
            return (x, y, z)
        return None

    def draw_shape(self, shape: Shape3D):
        self.clear()
        edges = self.get_edges(shape)
        projected_points = self.project_shape(shape)

        for start_idx, end_idx in edges:
            if projected_points[start_idx] and projected_points[end_idx]:
                self.draw_line(
                    projected_points[start_idx][0],
                    projected_points[start_idx][1],
                    projected_points[end_idx][0],
                    projected_points[end_idx][1],
                    shape.color
                )

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: str):
        # Drawing logic here

        def clear(self):
            self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def render(self) -> str:
        result = '\n'
        result += '┌' + '─' * self.width + '┐\n'
        for y in range(self.height):
            result += '│'
            for x in range(self.width):
                result += f"{self.colors[y][x]}{self.canvas[y][x]}{Style.RESET_ALL}"
            result += '│\n'
        result += '└' + '─' * self.width + '┘\n'
        return result
