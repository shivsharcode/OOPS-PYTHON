
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    
    def concrete(self):
        print("This is a concrete method")
    
    @abstractmethod
    def start(self):
        pass
    

class Car(Vehicle):
        
    def start(self):
        print("Car has started")
        
        

# we canot instantiate an Abstract class
v = Vehicle()  # ❌ TypeError: Can't instantiate abstract class Vehicle with abstract method start

c = Car()
c.start()
