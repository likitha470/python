class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img


    def num(self):
        print(self.real,"i+",self.img,"j")
    def __mul__(self,num2):#(ADD IS A DUNDER FUNCTION)
        newReal=self.real*num2.real  
        newImg=self.img*num2.img
        return Complex(newReal,newImg)
n1=Complex(4,3)
n1.num()

n2=Complex(7,8)
n2.num()

n3=n1*n2
n3.num()
           