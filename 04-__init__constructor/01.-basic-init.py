
class Student:
    def __init__(self, name, age):  # constructor
        self.name = name            # instance variable
        self.age = age              
        

s1 = Student("Shivam", 21)

print(s1.name, s1.age)



""""
behind the scenes when we write
s1 = Student("Shivam", 21)

Python does this internally:
s1 = Student.__new__(student)  # allocate memory
Student.__init__(s1, "Shivam", 21)  # initializes attributes
"""