#property-->we use thismethod in the class to use the method as a property
class Student:
    def __init__(self,phy,chem,math,):
        self.phy=phy
        self.chem=chem
        self.math=math
        # self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

    # def cal_percentage(self):
    #    self.percentage=str((self.phy+self.chem+self.math)/3)+"%"    
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"  
      

s1=Student(99,98,97) 

print(s1.percentage)  
s1.phy=86
# s1.cal_percentage()
print(s1.percentage)