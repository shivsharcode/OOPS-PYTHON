# in python it means : If an object has the methods/attributes you need, you can use it without checking its type
# the term comes from the phrase : "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck"

class Duck:
    def quack(self):
        print("Quack!")
        
class Person:
    def quack(self):
        print("I can imitate a duck!")
        

def make_it_quack(entity):
    entity.quack()
    

duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)


# 👉 here both 'duck' and 'person' can be passed to 'make_it_quack()' because they both implement 'quack()'.
#     their actual type doesn't matter