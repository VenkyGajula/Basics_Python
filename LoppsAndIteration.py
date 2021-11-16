print("*****While Loop(n natural numbers)*****")
n=5
while n>0 :
    print(n)
    n=n-1
print("End of the Loop")
print("*******for loop*******")
for i in range(1,5) :
    print(i)
print("*****break*****")
for i in range(1,10) :
    print(i)
    if(i == 8) :
        break

print("Loop Terminated")
print("*****Continue****")
for n in range(0,10) :
    print(n)
    if(n == 5) :
        continue
print("Loop is terminated")
print("****Summing******")
a=0
for i in [10,20,30,40,50] :
    a=a+i
print(a)
print("****Counting******")
count=0
for i in [10,20,30,40,50] :
    count=count+1
    print(count,i)
print("count =",count)
print("******Average*******")
count=0
sum=0
for i in [10,20,30,40,50] :
    count=count+1
    sum=sum+i
print("Average =",sum/count)
print("*******Exercise1*********")
n=0
total=0
while True :
    num=input("Enter the number")
    if num =='done':
        break
    try :
        n1=float(num)
    except :
        print("Invalid input")
        continue
    n=n+1
    total=total+n1
print("All done")
print(total,n,total/n)
print("*******Exercise 2")
count=0
sum=0
n=[11,22,33,44,55,66]
for i in n :
    count=count+1
    sum=sum+i
print("maximum =",max(n))
print("minimum =",min(n))
print("Average =",sum/count)
print("*******for Sample*********")
str=["venky",'hari','ramu','madhu']
for i in str :
    print("Welcome to Python", i)
print("Loop is completed")
