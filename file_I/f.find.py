def check_found(word):
   with open("practice.txt","r") as f:
    data=f.read()
    if data.find(word)!=-1:
      print("found")
    else:
     print("not found")

def check_line(word):
  
  data=True
  line=1

  with open("practice.txt","r") as f:
    while data:
      data=f.readline()
      if(word in data):
        print(line)
        
      line+=1
  return -1    


    
      
    
    
check_line("am")  
