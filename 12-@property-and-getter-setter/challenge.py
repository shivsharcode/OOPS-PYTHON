
class Temperature:
    
    def __init__(self, temp_celsius):
        self.__celsius = temp_celsius
            
    # getter
    @property
    def celsius(self):
        return self.__celsius
    
    # setter
    @celsius.setter
    def celsius(self, value):
        if value < -273:
            print("Invalid temperature")
        else:
            self.__celsius = value
            
    # deleter
    @celsius.deleter
    def celsius(self):
        print("Deleting temperature")
        del self.__celsius
        
    # another property
    @property
    def fahrenheit(self):
        F = ( self.__celsius * (9/5) ) + 32
        return F
    

t = Temperature(25)

print(t.celsius)  
print(t.fahrenheit)

t.celsius  = 30    # setter
print(t.celsius)
        
del t.celsius       # deleter for the attribute celsius

# print(t.celsius)    # AttributeError