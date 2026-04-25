
class Demo:
    def __str__(self):
        return "STR version"
    
    def __repr__(self):
        return "REPR Version"
    
    
d = Demo()

print(d)   # uses __str__
print([d])  # uses __repr__

# console > d    # uses __repr__