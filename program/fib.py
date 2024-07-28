n=10
f1=0
f2=1
f3=0
if(n==0):
    print(f1)
elif(n==1):
    print(f1,f2)
else:
    for i in range(1,n+1):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
