import math 

#도형 
class Shape : 
    cal_count = 0
    figure = "Shape"
    
    @classmethod
    def class_printFigure(cls) :
        return cls.figure
    
    @staticmethod 
    def static_printFigure() :
        return Shape.figure
    
    
#도형 상속 삼각형     
class Triangle(Shape) : 
    figure = "triangle"
    
    def __init__(self, b, h = 5) :
        self.b = b
        self.h = h
    
    def area(self) :
        Triangle.cal_count += 1
        
        return self.b * self.h / 2
    
#도형 상속 정삼각형 
class EquTriangle(Triangle) : 
    figure = "equilateral triangle"
    
    def __init__(self, a) : 
        self.a = a
        
    def area(self) : 
        EquTriangle.cal_count += 1
        
        return 0.25 * math.sqrt(3) * self.a ** 2
    
    def circumference(self) : 
        
        return self.a * 3
        
    
#도형 상속 원
class Circle(Shape) : 
    figure = "circle"
    
    def __init__(self, r) : 
        self.r = r
        
    def area(self) :
        Circle.cal_count += 1
        
        return math.pi * self.r ** 2
    
    def circumference(self) :         
        return 2 * math.pi * self.r
    
    
    
tri = Triangle(10, 4)
eqtri = EquTriangle(2)
cir = Circle(8)

print(cir.static_printFigure(), cir.area(), cir.circumference())
print(tri.class_printFigure(), tri.area(), cir.circumference())
print(eqtri.class_printFigure(), eqtri.area(), cir.circumference())

print(Shape.cal_count, cir.cal_count, tri.cal_count)