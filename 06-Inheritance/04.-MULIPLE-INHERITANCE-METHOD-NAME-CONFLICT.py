"""
If both the parent classes has methods with same name,
then that class method is inherited which is mentioned first (left to right) in the inheritance definition
THIS IS CALLED METHOD RESOLUTION ORDER (MRO)

# PRIORITY : class own's method >  parent class order (left to right)
"""

class Father:
    def skill(self):
        print("can drive")
        

class Mother:
    def skill(self):
        print("can cook")
        
        
# Child class
class Child(Mother, Father):   # method : skill will be inherited from Mother
    
    def talent(self):
        print("can swim")
    
    # def skill(self):     # highest priority
    #     print("can code")
    
c = Child()
c.skill()
c.talent()
        
        
