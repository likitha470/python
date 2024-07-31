class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_marks(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hi",self.name,"your avg marks:",(sum/3))

s1=Student("Likitha",[99,98,97]) 
s1.get_marks()  
s1.name="anitha"
s1.get_marks()  
s1.marks=[100,90,96]
s1.get_marks()

