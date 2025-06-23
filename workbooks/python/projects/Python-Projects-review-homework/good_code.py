from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    def __init__(self):
        pass
    @abstractmethod
    def get_area(self):
        raise NotImplementedError()
    @abstractmethod
    def get_length(self):
        raise NotImplementedError()


class ShapeException(Exception):
    def __init__(self, text):
        super().__init__(text)


class RightTriagle(Shape):

    def __init__(self, side_a, side_b, side_c):
        if not isinstance(side_a, int) or side_a <= 0:
            raise ValueError("side_a is not integer or <0")
        if not isinstance(side_b, int) or side_b <= 0:
            raise ValueError("side_b is not integer or <0")
        if not isinstance(side_c, int) or side_c <= 0:
            raise ValueError("side_c is not integer or <0")
        
        if not (side_a + side_b > side_c or side_a + side_c > side_b or side_b + side_c > side_a):
            raise ShapeException('Not triagle')
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return (self.side_a * self.side_b) / 2
    
    def get_length(self):
        return super().get_length


class Circle(Shape):

    def __init__(self, radius):
        if not isinstance(radius, int) or radius <= 0:
            raise ValueError("radius is not integer or <0")
        self.radius = radius

    def get_length(self):
        return 2 * pi() * self.radius
    
    def get_area(self):
        return super().get_area

