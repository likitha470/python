with open("D:\\python\\file_I\\file.txt","r") as f:#asias=f
    data=f.read()#no need of use f.close
    print(data)


with open("D:\\python\\file_I\\file.txt","w") as f:#asias=f
    data=f.write("new data")#no need of use f.close
    print(data)    