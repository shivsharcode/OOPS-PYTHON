# A CLASS CAN INHERIT FROM MULITPLE PARENT CLASSES.



class Father:
    def skill(self):
        print("Can Drive")
        

class Mother:
    def hobby(self):
        print("Can cook")
        
        
class Child(Mother, Father):
    def talent(self):
        print("Can code")
        

c = Child()

c.skill()
c.hobby()
c.talent()