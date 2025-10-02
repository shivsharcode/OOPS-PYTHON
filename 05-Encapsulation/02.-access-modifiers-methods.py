
class Student:
    
    # public method
    def study(self):
        print("Studying")
        
    # protected method  (name conventional only)
    def _calculate_rank(self):
        print("Internal logic for rank calculation")
        
    # private method (through name mangling)
    def __secret_formula(self):
        print("Hidden formula")
        
    
    def reveal(self):
        print("Revealing")
        self.__secret_formula()   # accessible inside the class
        

s1 = Student()

s1.study()          # public - ✅accessible everywhere
s1._calculate_rank()  # protected - ⚠️ will work but not conventional to use, only for internal use

# s1.__secret_formula()  # private  -❌ will give AttributeError
# s1._Student__secret_formula()  # name-mangled way to force access

s1.reveal()  # works ✅