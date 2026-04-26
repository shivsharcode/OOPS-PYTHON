

class Student:
    def __init__(self, total_marks):
        self.__marks = total_marks   # private attribute
        
        
    @property
    def percentage(self):
        return self.__marks  / 5
    
    
s = Student(450)

print(s.percentage)  # percentage acting as attribute