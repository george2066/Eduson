class Shape:
    """"""

    def __init__(self):
        """Constructor"""
        pass


    def getArea(this):
        pass
    
    def getLength(this):
        pass


class RightTriagle(Shape):

    def __init__(self, sideA, sideB, sideC): 
        self.A = sideA
        self.B = sideB
        self.C = sideC 
    

    def getArea(this):
        return (this.A*this.B) / 2


class Circle(Shape):

    def __init__(self, radius):
        self.R = radius
    
    def getLength(this):
        return 2*3.14*this.R