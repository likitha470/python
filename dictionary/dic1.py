null_dic={}
null_dic["name"]="likitha"
print(null_dic)
#nested dictionary
student={
    "name":"likitha",
    "subject":{
        "maths":98,
        "science":98,
        "social":99
    }

}
print(student["subject"]["maths"])#2 squre []

print(student.keys())#return all keys
print(student)
print(list(student.keys()))

print(len(student.keys()))
print(len(student["subject"]))
print(student.values())#returns all values


prin=list(student.items())
print(prin)#returns all key:value in theform of tuple


print(student["name"])#error
print(student.get("name2"))#None return the key acc value


new_dict={"city":"madikeri","name":"niharika"}
student.update(new_dict)#insert the specified value
print(student)