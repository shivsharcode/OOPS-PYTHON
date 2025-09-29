class Student:
    
    def __init__(self, name=None, age = None):
        self.name = name
        self.age = age
        
    def description(self):
        print(f"Student: {self.name}, Age: {self.age}")

s1 = Student("Shivam", 21)
s2 = Student("Aryan")     # age will be defualt to None here


s1.description()
s2.description()