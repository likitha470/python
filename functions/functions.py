#function(group of statement that perforns a specific task)
# def cal_sum(a, b):
#     s=a+b
#     print(s)
#     return s

# cal_sum(2,5)
# cal_sum(4,6)
# cal_sum(5,2)

def cal_sum(a,b):#fun definition;parameter
    return(a+b)

sum=cal_sum(3,6)#fun call;parameter
print(sum)

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()    
output=print_hello()
print(print_hello())#returns None