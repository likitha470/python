#used for sequential traversal
num=[1,2,3,4]
for val in num:
    print(val)

veg=("potato","carrot","tomato","onion","beans"  )#tuple
for items in veg:
    print(items)

str="likitha"
for val in str:
    if(val=="i"):

        print("i found")
        break
    print(val)
else:#requires when we use break
    print("end")    

