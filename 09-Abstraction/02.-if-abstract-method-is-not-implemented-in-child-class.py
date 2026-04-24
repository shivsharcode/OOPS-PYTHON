
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass
    
    
class Car(Vehicle):
    
    def drive(self):
        print("Car is driving")
        
    # not implemented the abstract method 'start'
    
    
c = Car()    # TypeError: Can't instantiate abstract class Car with abstract method start
c.drive()
        


