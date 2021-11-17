print("***Set Sample*****")
s={"Apple","banana","cherry","kiwi"}
print(s)#0/p-->{'kiwi', 'cherry', 'banana', 'Apple'}
#Duplicates are not allowed
s1={"Apple","banana","cherry","kiwi","Apple","kiwi","banana"}
print(s1)
#o/p--->{'Apple', 'banana', 'cherry', 'kiwi'}
print("****Find the Length****")
print(len(s))
print(len(s1))
#set Constructor
s2= set(("apple", "banana", "cherry"))
print(s2)
#Access items
r=('a','b','c','d')
for st in r:
    print(st)
print('a' in r)

#join Two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set4=set1.update(set2)
print(set4)
