import math

class Shape:
    def area(self):
        """
        Base class method for calculating area.
        Raises NotImplementedError to enforce overriding in derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Derived class Rectangle.
        Inherits from Shape and adds length and width attributes.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area() method to calculate the area of a rectangle.
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """
        Derived class Circle.
        Inherits from Shape and adds a radius attribute.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area() method to calculate the area of a circle.
        """
        return math.pi * (self.radius ** 2)