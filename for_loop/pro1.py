num=(1,4,9,16,25,36,49,64,81,100)
x=9
i=0
for val in num:
    if(val==x):
        print("found",i,val)
        break
    i+=1
else:
        print("not found")