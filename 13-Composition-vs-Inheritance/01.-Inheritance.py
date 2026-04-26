
# Inheritance ("IS-a" relationship)

# A class inherits from another when it is a type of that class.

class Animal:
    def speak(self):
        print("Animal speaks")
        
        
class Dog(Animal):   # Dog IS an Animal
    def bark(self):
        print("Dog barks")
        

d = Dog()
d.speak()
d.bark()


# Dog is-a Animal