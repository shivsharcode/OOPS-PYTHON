
class Book:
    def __init__(self, pages:int, author:str):
        self.pages = pages
        self.author = author
        
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"Book by {self.author}"
    
    
b = Book(300, "RR Narayan")

print(len(b))    # behavior bcoz of __len__ implementation

print(b)          # behavior bcoz of __str__ implementation