
class Student:
    # constructor
    def __init__(self, name, grade):
        self.name = name    # instance variable
        self.grade = grade  # instance variable
        
    # instance method
    def display_info(self):
        print(f"Student: {self.name}, Grade: {self.grade}")
        

# initiailize
student1 = Student("Shivam", 'B')
student2 = Student("Aryan", 'A')

# calling methods
student1.display_info(student1)
student2.display_info()