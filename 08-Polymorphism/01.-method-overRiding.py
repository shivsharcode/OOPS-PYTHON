
# METHOD OVER-RIDING 
# when the parent and child class both has method with same name
# the child method is priortized, since it over-rides the parent class method

class Animal:
    def speak(self):
        print("Animal speaks")
        
    def walk(self):
        print("Animal walks")
        
class Dog(Animal):
    def speak(self):
        print("Dog barks")
        

d = Dog()
d.speak()   # child method works
d.walk()   # inherited parent's method bcoz no over-riding