class Account:
    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc_no=acc_no
        print("total_amount:",self.get_bal())
     
    def debit(self,ammount):
        self.bal-=ammount
        print("rs",ammount,"was debited")
        print("total_amount:",self.get_bal())

    def credit(self,ammount)   :
        self.bal+=ammount 
       
    def get_bal(self):
        return self.bal  



acc1=Account(10000,123455)  
print(acc1.bal)
print(acc1.acc_no)             
acc1.debit (1000)
acc1.credit (20000)
