# s = "04.muliple-inheritance-method-name-conflict"
# s = "03.-multiple-inheritance"
# s = "01.-single-inheritance"
# print(s.upper())


# class Parent:
#     def __init__(self):
#         self.name = "Narayan"
#         print("Parent constructor")
        
#     def speak(self):
#         print("Parent speaking")
#         print(f"{self.name} is speaking")
        
        
# class Child(Parent):
#     def __init__(self):
#         print("Child Constructor")
#         super().__init__()
#         self.name = "Shiv"
        

# c = Child()
# c.speak()


        

# class Parent:
#     def __init__(self):
#         print("Parent class")
#         self.name = "Mummy"
  
#     def cook(self):
#         print("can cook")
        
#     def write(self):
#         print(f"{self.name} writes")
        

# class Child(Parent):
#     def __init__(self):
#         print("Child class")
        
#         super().__init__()
        
#         # self.name = "Shivam"
    
#         super().write()
    
        
# c1 = Child()
# c1.cook()



class Father:
    def __init__(self):
        print("Father Constructor")
        
        
class Mother:
    def __init__(self):
        print("Mother's Constructor")
        
        
class Child(Mother, Father):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

        
c = Child()
        