class Account:
    def __init__(self,acc_no,password):
        self.acc_no=acc_no
        self.__password=password  ####private
    def reset_password(self):
        print(self.__password)

acc1=Account("126749","gdjd67")
print(acc1.acc_no)
print(acc1.password)
