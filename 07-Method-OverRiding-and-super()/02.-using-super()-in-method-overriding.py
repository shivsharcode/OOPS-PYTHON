# super() in Method Overriding

class Employee:
    def display_info(self):
        print("This is an employee")
        

class Manager(Employee):
    def display_info(self):
        super().display_info()  # using super() to call parent's method, since due to method over-riding it wouldn't have worked otherwise
        print("This is a manager")
             

m = Manager()
m.display_info()