#text file
#binary file
#f=open("filename","mode")#"r","w"
f=open("D:\\python\\file_I\\file.txt","r")## Open the file using double backslashes
# data=f.read()#reads a entire file,#(3)=no of strings to read
# print(data)
line1=f.readline()#reads line by line
print(line1)
line2=f.readline()#reads line by line
print(line2)
# print(type(data))
f.close()

