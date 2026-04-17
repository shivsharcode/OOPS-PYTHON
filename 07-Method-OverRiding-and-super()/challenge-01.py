
class Shape:
    def describe(self):
        print("This is a shape")
        

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length =  length
        self.width = width
        
    def describe(self):   # method over-ride
        super().describe()   # call the parent class method
        print(f"This is a rectange with length {self.length} and width {self.width}")
        
    def area(self):
        return self.length * self.width
    

r = Rectangle(10, 5)
r.describe()
print("Area of rectange = ", r.area())