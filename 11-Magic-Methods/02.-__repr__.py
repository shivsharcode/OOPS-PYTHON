# __repr__ (Developer Friendly output)

class Student:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Student('{self.name}')"
    

s = Student("Shivam")
print(s)