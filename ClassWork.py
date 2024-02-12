class Rectangle:
    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

    def __str__(self):
        return " Rectangle with width " + str(self.width) + " Rectangle with height " + str(self.height)

    @staticmethod
    def get_info():
        return "This class calculates perimeter and area of the rectangles"

    def get_perimeter(self):
        per = 2 * (self.width + self.height)
        return per

    def get_area(self):
        area = self.width * self.height
        return area


print(dir(Rectangle))
print(Rectangle.get_info())

r1 = Rectangle(width=3, height=5)
print(r1)
print("perimeter:" + str(r1.get_perimeter()))
print("area:" + str(r1.get_area()))
class Square(Rectangle):
    def __init__(self, side=None):
        super().__init__(width=side, height=side)
        self.side = side

    def __str__(self):
        return "Square with side " + str(self.side)

    @staticmethod
    def get_info():
        return "This class calculates perimeter and area of the square"

    def get_square(self):
        resSquare = self.side ** 2
        return resSquare

print(Square.get_info())
s1 = Square(side=5)
print(s1)
print("Perimeter: " + str(s1.get_perimeter()))
print("Area: " + str(s1.get_area()))
print("Square: " + str(s1.get_square()))

class Cube(Square):
    def __int__(self, side = None):
        super().__init__(side=side)
    def __str__(self):
        return "Square with side " + str(self.side)
    def get_surfaceArea(self):
        SurArea = 6 * (self.side ** 2)
        return SurArea
    def get_volume(self):
        vol = self.side ** 3
        return vol

    @staticmethod
    def get_info():
        return "This class calculates surface area and volume of the cube"
print(dir(Cube))
print(Cube.get_info())
c1 = Cube(side = 10)
print(c1)
print("surface Area:" + str(c1.get_surfaceArea()))
print("Volume:" + str(c1.get_volume()))
