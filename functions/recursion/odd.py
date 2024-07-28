def odd(i):
    if(i>100):
        return
    if(i%2==0):
        odd(i+2)
        print(i)
    

odd(2)




    