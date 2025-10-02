class Student:
    def __init__(self, name):
        self.name = name  # Public
        
        self._marks = 90   # Protected, (convention only)
        
        self.__roll = 101  # private thorugh name mangling
   
   
   
        
s1 = Student("Alex")
print(s1.name)

print(s1._marks)

# print(s1.__roll)  # will give AttributeError

print(s1._Student__roll)  # works but "name mangling" trick