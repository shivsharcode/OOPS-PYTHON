
class Student:
    school_name = "SBV school"  # class variable
    
    def __init__(self, name):
        self.name = name
        
        
    @classmethod
    def change_school(cls, new_scl_name):
        cls.school_name = new_scl_name    # updating class variable
        

s1 = Student("Shivam")
print("School = ", s1.school_name)   # accessing class variable

Student.change_school("ABES")
# s1.change_school("ABES"), this can also update the same

print("School = ", s1.school_name)   # accessing class variable


