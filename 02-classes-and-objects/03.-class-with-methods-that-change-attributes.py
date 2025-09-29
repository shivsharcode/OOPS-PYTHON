
class Car:
    # constructor
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    # method - that change attribute
    def paint(self, new_color):
        self.color = new_color
        
    # method
    def drive(self):
        print(f"{self.color} {self.brand} is driving !")
        

if __name__  == '__main__':
    
    car1 = Car("Range Rover", "White")
    car1.drive()
    
    
    
    while True:
        choice = input("Do you want to paint your car to a new color (y/n): ").strip().lower()
        
        if choice == 'y':
            newColor = input("Enter new color: ").capitalize()
            car1.paint(newColor)
            car1.drive()
            break
            
        elif choice == 'n':
            print("Okay")
            car1.drive()
            break
        
        else:
            print("Invalid Input")
        
    print("End of Code")
    
    