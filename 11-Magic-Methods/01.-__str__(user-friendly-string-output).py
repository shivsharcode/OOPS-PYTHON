
# without __str__

"""
class Student:
    def __init__(self, name):
        self.name = name
        
        
s = Student("Shivam")
print(s)     # <__main__.Student object at 0xmemorylocation >

"""


# with __str__   (User friendly output)

class Student:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Student name: {self.name}"
       
    
s = Student("Shivam")
print(s)    

# python internally calls: object.__str__() and the returned value is printed