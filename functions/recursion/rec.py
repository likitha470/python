#when a function cass itself repeatedly(recursion)
def show(n):
    if(n==-1):#base case,stopping condition
         return
    print(n)
    show(n-1)#call stack(store layer by layer)
    print("end")
           

show(5)    