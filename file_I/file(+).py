# f=open("D:\\python\\file_I\\file.txt","r+")# read &OVERWRITE (pointer starting/no truncate)
# f=open("D:\\python\\file_I\\file.txt","w+")#truncated
f=open("D:\\python\\file_I\\file.txt","a+")#read&append(no truncate/pointer end)
f.write("abcs  ")
print(f.read())
f.close()