
# with open("practice.txt","w") as f:
#     data=f.write("2,4,67,84,83,56,43")
#     print(data)
    
count=0
with open("practice.txt","r") as f:#type cast to int
    data=f.readline()
    
    
    num=data.split(",")
    for value in num:
        if(int(value)%2==0):
            count+=1
print(count)            
            

    
    # num=""
    # for i in range(len(data)):
    #     if data[i]==",":
    #         print(int(num))
    #         num=""
    #     else:
    #         num+=data[i]
    # if i%2==0:
    #     print(count)
    #     count+=1
