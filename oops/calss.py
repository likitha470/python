#{decorators}
#1--->class method is bound to a class & recives the class as an implicit first argument.
#2--->static method can't access or modify class state & generally for the utitility
#3--->property


class Person:
    name="anonymous"
    def changename(self,name):
        self.name=name
        # self.__class__.name=name(change the name)
        # Person.name=name

p1=Person()
print(p1.name)
p1.changename("rahul")  
print(p1.name)
print(Person.name)
