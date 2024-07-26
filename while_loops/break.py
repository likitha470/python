i=1
while i<=5:
    print(i)
    if(i==3):
        break#here till 3 it prints
    i+=1
i=0
while i<=5:
    
    if((i%2)!=0):# for even
        i+=1
        continue # except 3 it prints or skipp
    print(i)
    i+=1
    
