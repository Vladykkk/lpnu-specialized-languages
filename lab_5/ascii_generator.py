import math
from dataclasses import dataclass
from typing import List, Tuple, Optional
from colorama import Fore, Style, init
import json
import os

@dataclass
class Point3D:
    x: float
    y: float
    z: float

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
        # 5 точок: 4 для основи і 1 для вершини
        points = [
            # Основа (квадрат)
            Point3D(-base_size/2, 0, -base_size/2),
            Point3D(base_size/2, 0, -base_size/2),
            Point3D(base_size/2, 0, base_size/2),
            Point3D(-base_size/2, 0, base_size/2),
            # Вершина піраміди
            Point3D(0, height, 0)
        ]
        super().__init__(points, color)

class Sphere(Shape3D):
    def __init__(self, radius: float = 1.0, segments: int = 8, color: str = Fore.WHITE):
        points = []
        # Генеруємо точки на сфері
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
        # Верхнє коло
        for i in range(segments):
            angle = (i * 2 * math.pi) / segments
            x = radius * math.cos(angle)
            z = radius * math.sin(angle)
            points.append(Point3D(x, height/2, z))
        
        # Нижнє коло
        for i in range(segments):
            angle = (i * 2 * math.pi) / segments
            x = radius * math.cos(angle)
            z = radius * math.sin(angle)
            points.append(Point3D(x, -height/2, z))
        
        super().__init__(points, color)

class ASCIIArtGenerator:
    def __init__(self, width: int = 40, height: int = 20):  # Зменшені розміри за замовчуванням
        self.width = width
        self.height = height
        self.canvas = [[' ' for _ in range(width)] for _ in range(height)]
        self.depth_buffer = [[float('inf') for _ in range(width)] for _ in range(height)]
        self.colors = [[Fore.WHITE for _ in range(width)] for _ in range(height)]
        init(autoreset=True)  # Автоматичний скид кольорів
        
    def project_point(self, point: Point3D) -> Optional[Tuple[int, int, float]]:
        z = point.z + 5
        if z <= 0:
            return None
        
        x = int(self.width/2 + (point.x * 100/z))  # Зменшений масштаб проекції
        y = int(self.height/2 + (point.y * 50/z))  # Зменшений масштаб проекції
        
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
        self.depth_buffer = [[float('inf') for _ in range(self.width)] for _ in range(self.height)]
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

class ASCII3DInterface:
    def __init__(self):
        self.generator = ASCIIArtGenerator()
        self.current_shape: Optional[Shape3D] = None

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
        if not self.current_shape:
            print("Спочатку створіть фігуру!")
            return

        while True:
            print("\nМаніпуляції з фігурою:")
            print("1. Перемістити")
            print("2. Масштабувати")
            print("3. Відобразити")
            print("4. Зберегти у файл")
            print("5. Вийти")
            
            choice = input("Виберіть опцію: ")
            
            if choice == "1":
                dx = float(input("dx (0): ") or 0)
                dy = float(input("dy (0): ") or 0)
                dz = float(input("dz (0): ") or 0)
                self.current_shape.translate(dx, dy, dz)
            
            elif choice == "2":
                scale = float(input("Коефіцієнт масштабування (1.0): ") or 1.0)
                self.current_shape.scale_shape(scale)
            
            elif choice == "3":
                self.generator.draw_shape(self.current_shape)
                print(self.generator.render())
            
            elif choice == "4":
                filename = input("Введіть ім'я файлу: ")
                self.generator.save_to_file(filename)
                print(f"Збережено у файл {filename}")
            
            elif choice == "5":
                break

def main():
    # Ініціалізуємо colorama для Windows
    init()
    
    print(Style.BRIGHT + "3D ASCII Art Generator" + Style.RESET_ALL)
    interface = ASCII3DInterface()
    
    while True:
        print("\nМеню:")
        print("1. Створити нову фігуру")
        print("2. Маніпулювати фігурою")
        print("3. Вийти")
        
        choice = input("Виберіть опцію: ")
        
        if choice == "1":
            interface.create_shape()
        elif choice == "2":
            interface.manipulate_shape()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()