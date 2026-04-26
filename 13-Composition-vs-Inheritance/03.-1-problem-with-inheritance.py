
class Bird:
    def fly(self):
        print("Flying")
        
        
class Penguin(Bird):
    def swim(self):
        print("Swimming")
        
        
peng = Penguin()
peng.swim()

peng.fly()   # Now Penguin can't fly, but inheritance forces it

# open code - 04: to see how Composition is better for such problem