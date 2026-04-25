
# THIS method will cause discrepencies in the way a CLASS VARIBALE should behave
# so it is preferrable to AVOID it

class Student:
    school_name = "SBV"
    
    # trying to update class var through Instance method
    def change_school(self, new_name):
        self.school_name = new_name   # ⚠️ it does NOT update the class variable
        
        
s1 = Student()
s2 = Student()

s1.change_school("ABES")

print(s1.school_name)   # ABES
print(s2.school_name)   # SBV

# ques1) why the school name is different for both the objects even though its a class variable (and thus update in class variable shuold be reflected in every objects of that class)

# Ans 
# : the self.school_name = new_name, creates a new Instance Variable, instead of updating the class variable
# so now, s1.school_name -> gives instance variable
# and s2.school_name -> still gives the class variable value

# ques2) Why this Happens ?

# Ans
# Python lookup order is like:
#   1. Check instance variables
#   2. Then check class variable
#   so assigning via 'self' creates a shadow copy


# SO BEST PRACTICE : is to update a class variable via 'Class method'