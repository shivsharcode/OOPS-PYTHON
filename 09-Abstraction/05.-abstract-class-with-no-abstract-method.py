from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def drive(self):
        print("Vehicle drive")
        
    # no abstract method
    

class Car(Vehicle):
    def stop(self):
        print("Car stops")
        
        

v = Vehicle()  # no TypeError, since Vehicle is actually not an abstract class until there is atleast 1 abstract method


c = Car()
c.stop()