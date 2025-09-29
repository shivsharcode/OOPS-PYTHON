import math
class Circle:
    
    # constructor
    def __init__(self, radius):
        self.radius = radius
        
    # instance method -1 
    def area(self):
        return math.pi * (self.radius ** 2)
    
    # instance method -2
    def circumference(self):
        return 2 * math.pi * self.radius
    
    
if __name__ == '__main__':
    c1 = Circle(3)
    c2 = Circle(5)
    
    print(f"c1 : Area = {c1.area()}, Circumference = {c1.circumference()}")
    print(f"c2 : Area = {c2.area()}, Circumference = {c2.circumference()}")
    