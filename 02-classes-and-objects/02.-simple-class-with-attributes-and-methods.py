
class Car:
    # constructor
    def __init__ (self, brand, color):
        self.brand = brand  # attribute
        self.color = color  # attribute
        
    # method
    def drive(self):
        print(f"{self.color} {self.brand} is driving !")
        
        
if __name__ == '__main__':
    
    # create objects (instances of Car)
    car1 = Car("Tata", "Blue")
    car2 = Car("Grand Vitara", 'Grey')
    
    # call methods
    car1.drive()
    car2.drive()