class Rectangle:
    def __init__(self):
        self.__width = None
        self.__height = None

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height


r1 = Rectangle()
r1.set_width(5)
r1.set_height(4)
print(r1.get_area())