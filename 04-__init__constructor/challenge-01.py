import datetime

class Person:
    
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        
    @classmethod
    def from_birth_year(cls, name:str, birth_year:int):
        age = datetime.datetime.now().year - birth_year
        return cls(name, age)
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
        

if __name__ == '__main__':
    p1 = Person("Shiv", 22)
    p2 = Person.from_birth_year("Aryan", 2000)

    p1.introduce()
    p2.introduce()
    

    
        
        

