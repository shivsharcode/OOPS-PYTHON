
class Student:
    # constructor
    def __init__(self, name:str, grade):
        self.name = name    # instance variables
        self.grade = grade  # instance variables
        

student1 = Student("Shivam", 'B')
student2 = Student("Aryan", 'A')

print(student1.name)
print(student2.name)