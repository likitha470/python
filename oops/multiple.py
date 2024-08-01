#multiple inheritance (base1,base2)
class A:
    varA="Welcome class A"
class B:
    varB="Welcome class B"
class C(A,B):
    varC="Welcome class C"     

c1=C()
print(c1.varC) 
print(c1.varB) 
print(c1.varA)      
