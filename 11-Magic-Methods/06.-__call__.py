# __call__  (Make object Callable)

class Greet:
    
    def __call__(self):
        print("Hello there!")
        

g = Greet()
g()     # obj behaves like function