# __add__ (Operator Overloading)


class Number:
    def __init__(self, value):
        self.value = value
        
    def __add__(self, other):
        return Number(self.value + other.value)
    
    
n1 = Number(5)
n2 = Number(10)

n3 = n1 + n2  
print(n3.value)    # 15


# here we just customised '+' operator

"""
# What python does here ? 

# when we write     a + b
# python actually does      a.__add__(b)
# so self is pointing to 'a' and other is pointing to 'b'
# and the method return a new object, Nummber(a.value + b.value)  = which is initialises an new object and return its reference
"""
