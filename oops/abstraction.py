#abstraction----->hiding implimentation of a class and only showing the essential features to the user
#encapusulation------>wrapping data and function to a single unit(object)
#inheritance
#polymorphism
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True    
        print("car started")

car1=Car()        
car1.start()

