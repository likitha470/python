class Person:
    name="anonymous"
    @classmethod
    def changename(cls,name):
        cls.name=name
        

p1=Person()
print(p1.name)
p1.changename("rahul")  
print(p1.name)
print(Person.name)