# __eq__   (object value Equality check)


# withot __eq__
"""
class Person:
    def __init__(self, name):
        self.name = name
        

p1 = Person("Govind")
p2 = Person("Govind")


print(p1 == p2)    # False, since it is checking the two objects equality, which are at different memory locations

print(p1)
print(p2)
"""


# with __eq__

class Person:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other):
        return self.name == other.name
    
    
p1 = Person("Nimai")
p2 = Person("Nimai")

print(p1 == p2)   # True, since __eq__ changes the behaviour of the inbuilt funtion and checks for the equality of the 'name' attribute


"""
when we write     `p1 == p2` here
what python actually does : 

p1.__eq__(p2),    thus  'self' points to 'p1' and 'other' points to 'p2',
and it return the boolean for p1.name == p2.name
"""
