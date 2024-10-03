import os
import math
from typing import Optional, Tuple
from point import Point3D
from shape import Shape3D
from colorama import Fore, Style, init

class ASCIIArtGenerator:
    def init(self, width: int = 40, height: int = 20):
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
        self.depthbuffer = [[float('inf') for _ in range(width)] for _ in range(height)]
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

        if isinstance(shape, Cube):
            edges = [
                (0, 1), (1, 2), (2, 3), (3, 0),  # Передня грань
                (4, 5), (5, 6), (6, 7), (7, 4),  # Задня грань
                (0, 4), (1, 5), (2, 6), (3, 7)   # З'єднувальні лінії
            ]
        elif isinstance(shape, Pyramid):
            edges = [
                (0, 1), (1, 2), (2, 3), (3, 0),  # Основа
                (0, 4), (1, 4), (2, 4), (3, 4)   # Ребра до вершини
            ]
        elif isinstance(shape, Sphere):
            segments = int(math.sqrt(len(shape.points)))
            edges = []
            # З'єднуємо точки в сітку
            for i in range(segments):
                for j in range(segments * 2):
                    current = i * segments * 2 + j
                    next_h = i * segments * 2 + (j + 1) % (segments * 2)
                    next_v = ((i + 1) % segments) * segments * 2 + j
                    edges.append((current, next_h))
                    if i < segments - 1:
                        edges.append((current, next_v))
        elif isinstance(shape, Cylinder):
            segments = len(shape.points) // 2
            edges = []
            # З'єднуємо точки верхнього і нижнього кіл
            for i in range(segments):
                next_i = (i + 1) % segments
                # Верхнє коло
                edges.append((i, next_i))
                # Нижнє коло
                edges.append((i + segments, next_i + segments))
                # Вертикальні лінії
                edges.append((i, i + segments))

        # Проектуємо всі точки
        projected_points = []
        for point in shape.points:
            transformed_point = Point3D(
                (point.x * shape.scale) + shape.position.x,
                (point.y * shape.scale) + shape.position.y,
                (point.z * shape.scale) + shape.position.z
            )

            projected = self.project_point(transformed_point)
            if projected is not None:
                projected_points.append(projected)
            else:
                projected_points.append(None)

        # Малюємо лінії між точками
        for start_idx, end_idx in edges:
            if (projected_points[start_idx] is not None and 
                projected_points[end_idx] is not None):
                self.draw_line(
                    projected_points[start_idx][0],
                    projected_points[start_idx][1],
                    projected_points[end_idx][0],
                    projected_points[end_idx][1],
                    shape.color
                )
        
      def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: str):
        """Малює лінію використовуючи алгоритм Брезенхема"""
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        if dx > dy:
            err = dx / 2.0
            while x != x2:
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.canvas[y][x] = '█'  # Використовуємо більш помітний символ
                    self.colors[y][x] = color
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y2:
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.canvas[y][x] = '█'  # Використовуємо більш помітний символ
                    self.colors[y][x] = color
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy

        if 0 <= x < self.width and 0 <= y < self.height:
            self.canvas[y][x] = '█'
            self.colors[y][x] = color
        
    def clear(self):
        self.canvas = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self.depthbuffer = [[float('inf') for _ in range(self.width)] for _ in range(self.height)]
        self.colors = [[Fore.WHITE for _ in range(self.width)] for _ in range(self.height)]

    def render(self) -> str:
        # Очищаємо екран перед рендерингом
        os.system('cls' if os.name == 'nt' else 'clear')

        result = '\n' # Додаємо відступ зверху
        # Додаємо рамку зверху
        result += '┌' + '─' * self.width + '┐\n'

        for y in range(self.height):
            result += '│'  # Ліва рамка
            for x in range(self.width):
                result += f"{self.colors[y][x]}{self.canvas[y][x]}{Style.RESET_ALL}"
            result += '│\n'  # Права рамка

        # Додаємо рамку знизу
        result += '└' + '─' * self.width + '┘\n'
        return result

    def save_to_file(self, filename: str):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.render())
