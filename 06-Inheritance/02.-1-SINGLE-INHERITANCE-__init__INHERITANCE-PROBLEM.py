
class Parent:
    def __init__(self):
        print("Parent constructor")
        
    def speak(self):
        print("Person speaking")
        
        
        
class Child(Parent):
    def __init__(self):
        print("Child constructor")
        

c = Child()  # parent constructor will not run, bcoz child class __init__ overrides the parent's.
c.speak()    # inherits from parent