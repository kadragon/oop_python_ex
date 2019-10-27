# 추상 메소드 선언을 위하여 사용하는 패키지
from abc import *


class Figure:
    @abstractmethod  # 추상 메소드 선언 | 반드시 구현해야할 Method 임을 명시
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total


shapes = [Rectangle(1, 6), Rectangle(2, 3), Circle(5), Circle(7)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area())
