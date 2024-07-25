#dictionary are used to store data in key:value pairs
#word(key):meaning(value)
info={
    "key":"value",
    "name":"likitha",
    "learning":"coding",
    "subjects":["phython","c","java"],
    "topic":("dictionary","set"),
    "marks" : 35,
    "age":20,
    "is_adult":True
}
print(type(info))#these are unorderded,#no index ,#mutable,#no duplicate key
print(info)
print(info["subjects"])
info["name"]="rai"
info["surname"]="liki"# adding extra key
print(info)
