import math

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def decribe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}.")
    
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"It is a circle with an area of {3.14 * math.pow(self.radius, 2)}")
        super().decribe() #This calls the parent class method
    
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled, width)
        self.width = width
        self.height = height

circle = Circle(color = "red", is_filled = True, radius = 5)
circle.describe()