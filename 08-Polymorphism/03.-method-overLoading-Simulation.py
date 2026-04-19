# Python does NOT support traditional method overloading
# we simulate it

# method overloading = Same method name with different parameters performs differently

class Maths:
    
    # simulation of method-overloading
    def add(self, a, b, c= 0):
        return a + b + c
    
    
m = Maths()
print( m.add(2, 3) )     # works
print( m.add(2, 3, 4) )  # works