# list=[2,89,63,65]
# max=list[0]

# for i in list:
#     if(i>max):
#         max=i
#         i+=1
        
# print("max",max)
import array as arr

list=[1,2,7,45,89,3,56]
# largest=-1
# temp=-1
# for i in list:
#   if(largest<i):
#     b=temp
#     temp=largest
#     largest=i
  
# print(largest)
# print(temp)
# print(b)

# list2=list.sort()
# list2=sorted(list)
# print(list2[len(list2)-2])


for i in list:
    for j in list:
        if(i<i-1):
            temp=list[j]
            list[]=list[i+1]
            list[i+1]=temp
print(list)


