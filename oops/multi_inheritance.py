#multi level inheritance(base-->derived-->derived)
class Car:
    # @staticmethod
    def start():
        print("car started..")

    # @staticmethod
    def stop():
        print("car stopped.")


class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type   

car1=Fortuner("desel")
print(car1.stop())
