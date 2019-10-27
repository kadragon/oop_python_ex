# 가로, 세로를 입력 받아 사각형 객체를 구현
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


# 넓이를 계산해주는 클래스
class AreaCalculator(object):
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.width * shape.height
        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area())
