# 나쁜 예
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


class AreaCalculator(object):
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            if type(shape) == Rectangle:
                total += shape.width * shape.height
            elif type(shape) == Circle:
                return 3.14 * shape.radius ** 2
        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6), Circle(1.5)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area())
