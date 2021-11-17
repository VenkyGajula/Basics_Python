#Dictionary Sample Program
bag=dict()
bag['chacolates']=10
bag['books']=20
bag['pens']=30
bag['chargers']=5
print(bag)
print(bag['pens'])
#Dictionary Literals(Constants)
data={'date':8,'month':3,'year':2021,'Yop':2020,'Course':'MCA','college':'vidyanikethan'}
print(data)
#Empty dictionary
a={}
print(a)
#MAny counters with a dictionary
cnt=dict()
cnt['maths']=1
cnt['pysics']=1
print(cnt)
cnt['pysics']=cnt['pysics']+1
print(cnt)
print("*********")
counts=dict()
names={'venky','Ramu','Hari','venky','Ravi'}
for name in names :
    if name not in counts :
        counts[name]=1
    else :
        counts[name]=counts[name]+1
print(counts)
# get() for dictionaries
if name in counts :
    x=counts[name]
else :
    x=0
x=counts.get(name,0)
print(x)
#counting with get()
counts=dict()
nam={'v','r','g','f','r','v'}
for name in nam :
    counts[name]=counts.get(name,0)+1
print(counts)
#counting Pattern
counts=dict()
print('Hello Welcome to python')
line=input('')
words=line.split()
print('words:',words)
print('counting...')
for word in words :
    counts[word]=counts.get(word,0)+1
print('counts',counts)
#Retrieving Lists of Keys and Values
info={'name':'Venky','Age':24,'Qualifi':'MCA','YOP':2020}
print(info)
k=info.keys()
print(k)
v=info.values()
print(v)
i=info.items()
print(i)
print("******Exercise******")
name='GajulaVenkateshwarlu'
counts=dict()
for nam in name :
    if name not in counts :
        counts[nam]=1
    else :
        counts[nam]=counts[nam]+1
print(counts)
