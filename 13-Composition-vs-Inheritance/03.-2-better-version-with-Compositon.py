
class CanFly:
    def fly(self):
        print("Flying")
        

class CannotFly:
    def fly(self):
        print("Cannot Fly")
        
        
class Bird:
    def __init__(self, fly_behavior):
        self.fly_behavior = fly_behavior
        
    def perform_fly(self):
        self.fly_behavior.fly()
        
        
        
sparrow = Bird(CanFly())
penguin = Bird(CannotFly())

sparrow.perform_fly()  # Flying
penguin.perform_fly()  # Cannot Fly