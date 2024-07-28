def recursion(i,a):
    if(i>21):
        return
    recursion(i+1,a)
    print(i*a)

recursion(1,5)    