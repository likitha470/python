collection=set()

collection.add(89)#hashable 
collection.add((1,5,7,8))
collection.add("likitha")

print(collection)
collection.remove(89)
collection.clear()
print(collection)
print(len(collection))#0

# collection.pop()
# print(collection)

coll={6,9,0,8,87,"liki","lojh"}
coll.pop()
print(coll)
bon={9,0,7,678,987}
#union
print(bon.union(coll))
print(bon.intersection(coll))

