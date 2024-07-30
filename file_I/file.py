#text file
#binary file
#f=open("filename","mode")#"r","w"
f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))