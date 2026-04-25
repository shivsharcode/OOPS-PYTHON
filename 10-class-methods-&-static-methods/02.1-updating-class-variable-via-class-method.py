
"""
✅ This is the correct way of updating the class variables -i.e through class methods
"""


class Student:
    school_name = "SBV"  # class variable
    
    # class method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        

s1 = Student()
s2 = Student()

s1.change_school("ABES")

print(s1.school_name)
print(s2.school_name)
    
    
# NOTE : 
# BOTH objects see the change, since the change is in class varible
# which belong to the class, not specific to any single object


# NOTE-2
    # this would've worked as well
    # def change_school(self, new_name):
    #   Student.school = new_name     # through class name not through self
        
    