# USING super() FOR INHERITING PARENT'S __init__

class Parent:
    def __init__(self):
        print("Parent constructor")
        
    def speak(self):
        print("Person speaking")
        

class Child(Parent):
    def __init__(self):
        super().__init__()  # call's parent's __init__
        print("Child constructor")
        
        
c = Child()  # both the constructors (viz. Parent, Child) will run due to super().__init__()
c.speak()   # inherits from Parent