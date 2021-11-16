print("*******Concatenation*******")
str1="Gajula"
str2="Venkateshwarlu"
Name=str1+str2
print("Welcome to Python ",Name)
print("*****string converting numbers")
a='123'
n=int(a)+1#o/p-->124
print(n)
print("*****find the String Length*********")
str="venkatesh"
length=len(str)
print("Length of str is =",length)
print("****get single character****")
fruit="Mango"
ch=fruit[0]
ch1=fruit[1]
ch2=fruit[2]
ch3=fruit[3]
print(ch,ch1,ch2)
print("Looping through String")
str="Madhukumar"
index=0
while index<len(str) :
    ch=str[index]
    print(index,ch)
    index=index+1
print("**********")
#Using for Looping
str1="banana"
count=0
for ch in str1 :
    count=count+1
    print(count,ch)
print("Looping is completed")
print("***Repeating letter counting******")
str2='aaaabbcc'
count1=0
for ch in str2 :
    if ch=='a' :
        count1=count1+1
print("Counting =",count1)#---->o/p---->4
print("****String Slicing*********")
s="Gajula Venakteshwarlu"
Slicing=s[0:11]
Slicing1=s[2:12]
Slicing2=s[:5]
Slicing3=s[8:]
Slicing4=s[:]
print(Slicing)
print(Slicing1)
print(Slicing2)
print(Slicing3)
print(Slicing4)
print("***using IN operator******")# it gives Boolean value
ch=input("Enter the character")
str='Ramakrishna'
if ch in str :
    print("True")
else :
    print("False")
print("**converting upper and lower****")
str="VEnkatesh"
cap=str.upper()
smaller=str.lower()
print("Capital =",cap)
print("Smaller =",smaller)
print("********String Searching find()****")
str="banana"
pos=str.find('ba')
print(pos)
a=str.find('na')
print(a)
print("*****Replace****")
str="Venkatesh g"
rs=str.replace('g',"Gajula")
print(str)
print(rs)
str1="Hello world"
rs1=str1.replace('o','Y')
print(str1)
print(rs1)
print("****Stripping WhiteSpace")
str=" Rama and sitha "
s=str.lstrip()
s1=str.rstrip()
s2=str.strip()
print(str)
print(s)
print(s1)
print(s2)
print("***Prefixes***")
str='Please give me a pen'
op=str.startswith('Please')
op1=str.startswith('p')
print(op)
print(op1)
print("********Parsing and Extracting")
str="venky@gmail.com from jan 01 2018"
atpos=str.find("@")
print(atpos)
sppos=str.find(' ',atpos)
print(sppos)
host=str[atpos+2 : sppos]
print(host)
print("*****Excercise**********")
str='X-DSPAM-Confidence:0.8475'
begin=str.find(':')
stop=len(str)
num=str[begin+1:stop]
fnum=float(num)
print(num)
