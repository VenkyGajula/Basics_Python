#tuples Sample**********
names=('venky','hari','Ravi','Guru','Ramesh')
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
num=(1,2,3,4,5,6,7,8,9)
print(num)
print(max(num))
print(min(num))
for i in num :
  print(i)
for y in names :
  print(y)
print("*******Tuples are Immutable********")
#so we are converting tuple to List
lis=list(names)
lis.append("mehaswi")
names=tuple(lis)
print(names)
li=list(num)
li.insert(0,55)
num=tuple(li)
print(num)
l=list()
print("****List********")
print(dir(l))
print("******Tuple*****")
t=tuple()
print(dir(t))
print("*******Tuples and Assignment*********")
(x,y,z)=("venky",'Hari','Ramesh')
print(x)
print(y)
print(z)
print("*****Sorting Lists of Tuples*********sorted()***")
fruits={"apple":1,"banana":5,"kiwi":3}
print(fruits.items())
print("******Comparing Tuples******")
print((0, 1, 2) < (0, 3, 4))
print((0, 1, 2000000) < (0, 3, 4))
print("*****Exercise******")
d= dict()
lst = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'Even':
        continue
    else:
        if words[1] not in d:
            d[words[1]] = 1
        else:
            d[words[1]] += 1

for key, val in list(d.items()):
    lst.append((val, key))

lst.sort(reverse=True)                  # Sorts by highest value

for key, val in lst[:1]:                # Only displays the largest value
    print(key, val)
print("******Exercise*******")
dh= dict()
lst = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'Even':
        continue

    col_pos = words[5].find(':')
    hour = words[5][:col_pos]
    if hour not in dh:
        dh[hour] = 1# First entry
    else:
        dh[hour] += 1# Additional counts

for key, val in list(dh.items()):
    lst.append((key, val)) # Fills list with hour, count of dict

lst.sort()# Sorts by hour

for key, val in lst:
    print(key, val)
