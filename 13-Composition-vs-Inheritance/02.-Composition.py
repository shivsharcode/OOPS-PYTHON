# Composition  ("HAS-a" relationship)

# A class contains another obect instead of inheriting from it.

class Engine:
    def start(self):
        print("Engine started")
        

class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS an Engine
        
    def start(self):
        self.engine.start()
        print("Car is moving")
        
        
car = Car()
car.start()


# Car has-a Engine