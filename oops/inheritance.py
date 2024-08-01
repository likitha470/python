#when one class derives the properties & method of another class(parent/base)
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortune")
car2=ToyotaCar("prius")     

print(car1.start())
print(car2.start())


#single inheritance(base-->derived)
#multi level inheritance(base-->derived-->derived)

