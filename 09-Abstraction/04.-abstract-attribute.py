
"""
Abstract attributes: 
    * Declared as required attributes in an ABC.
    * should be implemented in subclasses otherwise instantiation fails
    
    * we can enforce abstract attributes using the '@abstractmethod' decorator on a property
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    # abstract attribute
    @property
    @abstractmethod
    def color(self):
        pass
    
    
class Car(Vehicle):
    
    # implementing the abstract attribute in  the child class
    @property
    def color(self):
        return "Bluish Black"
    

c = Car()
print(c.color)  # attribute


# note: just like abstractmethod, it is Necessary to implement the abstract attribute in the child class Otherwise interpreter would throw 'TypeError'
