import math

class Shape():
    def area(self):
        pass   
     
    def perimeter(self):
        pass
        
class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError ("Parameters must be a positive number!")
        self.radius = float(radius)
        
    def area(self):
        A=math.pi*float(self.radius*self.radius)
        print("The area of the circle is",A," units squared.")
        
    def perimeter(self):
        P=2*math.pi*float(self.radius)
        print("The perimeter of the circle is",P,"units.")
        
class Triangle(Shape):
    def __init__(self, sideA, sideB, base, height):
        if sideA <= 0 or sideB <= 0 or base <= 0 or height <= 0:
            raise ValueError ("Parameters must be a positive number!")
        self.sideA = float(sideA)
        self.sideB = float(sideB)
        self.base = float(base)
        self.height = float(height)
        
    def area(self):
        A=(self.base*self.height)/2
        print("The area of the triangle is",A," units squared.")
        
    def perimeter(self):
        P = self.sideA+self.sideB+self.base
        print("The perimeter of the triangle is",P,"units.")            
            
class Rectangle(Shape):
    def __init__(self, length, height):
        if length <= 0 or height <=0 :
            raise ValueError ("Parameters must be a positive number!")
        self.length = float(length)
        self.height = float(height)
        
    def area(self):
        A=self.length*self.height
        print("The area of the rectangle is",A," units squared.")
    
    def perimeter(self):
        P=2*(self.length+self.height)
        print("The perimeter of the rectangle is",P," units squared.")
        

circle = Circle(5)
Circle.area(circle)
Circle.perimeter(circle)

H = math.sqrt(18.75)
triangle = Triangle(5,5,5,H)
Triangle.area(triangle)
Triangle.perimeter(triangle)

rectangle = Rectangle(5, 5)
Rectangle.area(rectangle)
Rectangle.perimeter(rectangle)

