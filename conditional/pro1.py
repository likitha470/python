marks=int(input("enter the mark of the student"))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="c"
else:
    grade="d"
print("grade of the student-->",grade)
