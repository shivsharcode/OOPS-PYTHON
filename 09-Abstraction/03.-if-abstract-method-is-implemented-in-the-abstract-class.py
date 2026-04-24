
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        print("Vehicle started")  # abstract method implemented in abstract class
        
        
class Car(Vehicle):
    
    def start(self):
        print("Car started")
    
    
c = Car()
c.start()


# why does it works?
# Ans)  In Python: Abstract methods CAN have implementation(body), this is different from many languages like Java.

# what '@abstractmethod' Actually means:
# Ans) It does NOT mean : "❌ This method must be empty"
# it means : ✅ This method MUST be overridden in child classes before object creation.

# but it's a convention and safe that abstract method should be empty