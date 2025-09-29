class Test:
    count = 0  # class variable (shared accross all objects)
    
    def __init__(self, subject):
        self.subject = subject   # instance variable
        Test.count += 1         # class variable
        
    
t1 = Test('English')
t2 = Test('Hindi')


print(Test.count)