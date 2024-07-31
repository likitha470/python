#all class have a function called _init_(),which is always excicuted when a class is being initiated.
class Student:
    college_name="MITE"
    def __init__(self,name,mark):#self(default) constructor
     pass   
#parameterized constructer
    def __init__(self,name,mark):#self is a reference
        self.name=name
        self.mark=mark
        print(self)
        print("Adding new student in Database")

s1=Student("likitha",90)#instance or object
print(s1.name,":",s1.mark,":",s1.college_name)    
s2=Student("karan",99)
print(s2.name,":",s2.mark,":",s2.college_name)