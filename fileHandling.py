file=open("C://Users/user/Desktop/sample.txt","r")
file1=file.read()
print(file1)
file.close()
print("***newlLine*****")
stuff='Gajula\nVenkateshwarlu'
print(stuff)
print(len(stuff))
print("***Counting*****")
count=0
for f in file :
    count=count+1
    print(count)
print("***Exercise*****")
file=open("C://Users/user/Desktop/sample.txt","r")
for line in file :
    line=line.rstrip()
    line=line.upper()
    print(line)
