
class Student:
    # instance method constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # class method as alternative constructor
    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))
    
    
s1 = Student("Shivam", 22)
print(f"Name = {s1.name}, Age = {s1.age}")

s2 = Student.from_string("Govind-16")
print(f"Name = {s2.name}, Age = {s2.age}")
