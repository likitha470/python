nums = (1,4,9,16,25,36,49,64,81,100)

x=36

i=0
while i<len(nums):
    if(nums[i] ==x):
        print("found",i)
        break 
    else:
        print("not found")      
    i+=1