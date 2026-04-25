
class Number:
    def __init__(self, value):
        self.value = value
        
        
n1 = Number(5)
n2 = Number(10)

n3 = n1 + n2       # TypeError : unsupported operand types(s) for +: 'Number' and 'Number'

print(n3.value)