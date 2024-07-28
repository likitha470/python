str="mom"
length=len(str)
i=length-1
str2=""
# print(i)
while(i>-1):
    # print(str[i])
    str2+=str[i]
    i-=1
print(str2)
if(str==str2):
    print("true")

