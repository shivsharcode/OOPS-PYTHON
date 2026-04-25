# Ques: Why not just use normal functions instead of static methods

# Ans) see, the whole point of static methods are : they logically belong to the class, that is they could act as 
# helper functions for the class, and could improve the code maintainability and structure
# in this way the objects of the class could also use static methods like normal mehtods

# but if we make normal functions without @staticmethod in the class, though it may work when called through
# class.methodname , but the objects of that class can't access it,
# That is the reason why we use 'static methods' instead of making normal functions

class Vehicle:
    
    # instance method
    def start(self):
        print("Vehicle started")
        
    # a normal function - not instance, not class, not static
    def stop():
        print("Vehicle stopped")
        
    @staticmethod
    def horn():
        print("Vehicle horn is blown")
        

Vehicle.start()
Vehicle.stop()       # class can access normal function
Vehicle.horn()      # class can access static method

car = Vehicle()     
 
car.start()         # works
car.horn()          # works  - object of the class can access the static method
car.stop()          # NOT works   - TypeError , -object can't access this normal function