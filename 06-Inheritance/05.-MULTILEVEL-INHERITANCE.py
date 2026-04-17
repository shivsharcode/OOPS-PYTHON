# A CHAIN OF INHERITANCE

class Grandparent:
    def house(self):
        print("Has a house")
        
        
class Parent(Grandparent):
    def car(self):
        print("Has a car")
        

class Child(Parent):
    def bike(self):
        print("Has a bike")
        
        
c = Child()
c.house()   # from Grandparent
c.car()     # from parent
c.bike()    # child's own