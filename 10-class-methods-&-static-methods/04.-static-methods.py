
# static methods

class BankApp:
    
    def login(self):
        print("Device logging to Bank")
    
    @staticmethod
    def add(a, b):
        return a + b
    
"""
# now It could be noted that, there isn't a necessary that the add method should be in the class, as it doesn't needs to access and update the instance/class values
# but it could be seen that it can logically belong to the class, that if it Is there, the code becomes complete and well maintained
# that's where static method comes in

# they act as utility/helper function
# but they don't access or update object/class data
"""



# no need to create object for accessing static method
print(BankApp.add(5, 6))

# but objects can also access static methods of the class
person1 = BankApp()
print(person1.add(2, 3))