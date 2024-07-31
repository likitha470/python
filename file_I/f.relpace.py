# with open("practice.txt","r+") as f:
#   f.write("Hi everyone\n")
#   f.write("we are learning File I/O\n")
#   f.write("using java.\n")
#   f.write("l like programming in java\n")

with open("practice.txt","r") as f:
  data=f.read()
  print(data)
  new=data.replace("java","python")
  print(new)
  

with open("practice.txt","w") as f:
  f.write(new)
  


    

