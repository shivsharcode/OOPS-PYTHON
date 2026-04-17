# one child class inherits from one parent class

# Parent
class Animal:
    def speak(self):
        print("Animal speaks")
        
        
# Child Class
class Dog(Animal):    # inherits Animal class
    def bark(self):
        print("Dog barks")
         
        
d = Dog()
d.speak()   # inherited from Animal class
d.bark()    # Dog's own method
