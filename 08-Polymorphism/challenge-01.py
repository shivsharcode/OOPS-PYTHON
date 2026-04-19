# Duck- typing challenge, same function name behaves differently as per the object

class UPI:
    def pay(self, amount):
        print(f"Paid {amount} using UPI")
        

class Card:
    def pay(self, amount):
        print(f"Paid {amount} using Card")
        
        
class Cash:
    def pay(self, amount):
        print(f"Paid {amount} using Cash")
        
        
def make_payment(method, amount):
    method.pay(amount)
    
    
upi = UPI()
card = Card()
cash = Cash()

make_payment(upi, 1000)
make_payment(card, 2000)
make_payment(cash, 500)