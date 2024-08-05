list=[1,2,3,4,5]

# def swap(a,b,):
#     tem=a
#     a=b
#     b=tem
#     print("the two element",a,b)
#     print(list)

# swap(a,b)  

def swap(list,a,b):
    print(list)
    list[a],list[b]=list[b],list[a]
    print(list)

swap(list,0,4)    