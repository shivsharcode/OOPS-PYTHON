
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
        
    
class Manager(Employee):
    def __init__(self,name, salary, department):
        super().__init__(name, salary)        # initializes the parent's __init__ to inherit the attributes
        self.department = department
        
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")
        

m1 = Manager("Shiv", 50000, "Engineering")
m1.display_info()