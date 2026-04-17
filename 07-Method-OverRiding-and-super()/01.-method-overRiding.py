# Method Over-Riding : child method over-rides the parent's version

class Animal:
    def speak(self):
        print("Animal makes a sound")
        
class Dog(Animal):  
    def speak(self): #same name as parent's method --> child method will override
        print("Dog barks")
        
        
a = Animal()
a.speak()

d = Dog()
d.speak()    # child method is executed because of method overriding