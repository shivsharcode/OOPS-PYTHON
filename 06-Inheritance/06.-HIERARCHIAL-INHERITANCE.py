# One parent, multiple children

class Parent:
    def house(self):
        print("Has a house")
        

class Son(Parent):
    def play(self):
        print("Plays wrestling")
        

class Daughter(Parent):
    def cook(self):
        print("Can cook")
        

s = Son()
d = Daughter()

# son 
s.house()       # inherited 
s.play()


# daughter
d.house()      # inherited
d.cook()

