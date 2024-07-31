#static method dont use the self parameter#works at class level
class Student:
    college_name="MITE"

    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        print(self)
        print("Adding new student in Database")

    @staticmethod###decorator
    def welcome():
        print("welcome ")

    def get_marks(self):
        return self.mark    
    
s1=Student("likitha",90)
s1.welcome()
print(s1.get_marks())
print(s1.name,":",s1.mark,":",s1.college_name)   

s2=Student("karan",99)
s2.welcome()
print(s2.get_marks())
print(s2.name,":",s2.mark,":",s2.college_name)    