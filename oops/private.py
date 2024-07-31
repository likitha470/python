#private attributes are used only within the class and are not accessible from outside the class
class Person:
    __name="annonymous"
    def __hello(self):
        print("hello person!")
    def welcome(self):
        self.__hello()    

p1=Person()    
print(p1.welcome())
