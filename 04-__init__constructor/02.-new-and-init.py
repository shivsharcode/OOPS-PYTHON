class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

s1 = Student.__new__(Student)        # 01 allocates memory

print(s1)
#print(s1.name) # will throw error

Student.__init__(s1, "Shivam", 21)   # 02 initializes attributes

print(s1)
print(s1.name)
print(s1.age)