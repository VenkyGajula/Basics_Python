print("*****List Sample****")
count=0
fruits=["Banana","MAngo","cherry","Grapes"]
print(fruits)
for a in fruits :
    count=count+1
    print(count,a)
print("****Lists and Definite Loops******")
friends=['venky','madhu','hari','Ravali']
for friend in friends :
    print("Happy newYear :",friend)
print("Done!")
print("***Looking Inside Lists****")
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print("****List are Mutable")
a=[1,2,3,4,5,6,7,8,9,]
print(a)
a[0]=10
a[1]=11
a[2]=12
print(a)
print("*******Find the length of the List*******")
names=['venky','Ravali','MAlli','Madhu','Srinu','PAvan','RAvi']
length=len(names)
print(length)
print("****Range of the List*******")
print(range(5))
frnd=['v','r','g','d','w','p','x','a']
print(range(len(frnd)))
print("***Concatenating Lists****")
a=[3,6,9,8,5,2,1]
b=[5,2,3,6,9,4,5]
c=[0,1,2,3,8,5,6,9]
d=a+b+c
print(d)
print("****List Can be Sliced : *********")
n=[1,2,3,6,5,4,9,8,7,10]
s=n[5:8]
s1=n[:4]
s2=n[6:]
s3=n[:]
print(s)
print(s1)
print(s2)
print(s3)
print("****List Methods*****")
a=list()
b=type(a)
c=dir(a)
print(b)
print(c)
print('*****Building a List From Scratch ****')
stuff=list()
stuff.append('Gajula')
stuff.append('Venkatesh')
stuff.append("MCA")
print(stuff)
stuff.append('Sri vidyanikethan Institue')
print(stuff)
print("***List are in Order****")
a=[55,4,2,1,88,33,66,99,42,58,5]
print(a.sort())
print(a[3])
print("****Built in Functions****** ")
num=[1,2,3,4,5,6,7,8,9]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/len(num))
print("****split****")
str="I need a Help"
stuff=str.split()
print(stuff)
print(len(stuff))
for s in stuff :
    print(s)
str='v;e;n;k;y'
st=str.split()
print(st)
st1=str.split(';')
print(st1)
for i in st1 :
    print(i)
print("****List Operators****")
v=[2]*4
print(v)
a=[1,2,3,4]
b=[5,6,7,8]
c=a.extend(b)
print(c)
