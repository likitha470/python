#super method is used to access method of the parent class(inheritance-->parent)
#### super().__init__(type)####
class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")


class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()

car1=ToyotaCar("fortune","electric")
print(car1.type)  


# class Car:
#     def __init__(self, type):
#         self.type = type

#     def start(self):
#         print("car started..")

#     def stop(self):
#         print("car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         self.start()  # Call start as an instance method

# car1 = ToyotaCar("fortune", "electric")
# print(car1.type)


