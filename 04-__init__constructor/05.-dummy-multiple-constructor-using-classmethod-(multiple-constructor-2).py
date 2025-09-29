
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_string(cls, data):
        name, age = data.split('-')
        return cls(name, int(age))
    
    
s1 = Student("Shivam", 22)
s2 = Student.from_string("Aryan-20")

print(s2.name, s2.age)


"""
ques) what is 'cls' ?
Ans : In Python, cls is not a keyword. It is just a naming convention used for the first parameter of a @classmethod.

In a @classmethod, the first parameter refers to the class itself, not an instance.
By convention, this parameter is named cls (short for "class"), just like self is used for instance methods.
What is it doing?

cls allows you to access the class and create new instances of it.
In your code, cls(name, int(age)) creates a new Student object using the class constructor.
So, cls is simply a reference to the class (Student in this case), and is used to create or manipulate class-level data.

"""