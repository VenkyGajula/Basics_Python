x=int(input("Enter the Number"))
if x<20:
  print("given Number is smaller than 20")
if x>20:
  print("Number is bigger than 20")
print("finish")
print("****Sample try/except ******")
number=input("Enter the data")
try :
    num1=int(number)
except :
    num1=-1
if num1>0 :
    print("Number")
else :
    print("String")
print("****Execise 6*****")
h=input("Enter the hour ")
try :
    hr=int(h)
except :
    print("Error, please Enter the numeric input")
r=input("Enter the rate")
try :
    rr=int(r)
except :
    print("Error, please Enter the numeric input")
#print("pay :",hr*rr*15)
print("********Exercise 7******")
x=float(input("enter the Score"))
if x>=10 :
    print("Bad Score")
elif x>=0.9 and x<=0.99 :
    print("A")
elif x>=0.8 and x<=0.89 :
    print("B")
elif x>=0.7 and x<=0.79 :
    print("C")
elif x>=0.6 and x<=0.69 :
    print("D")
elif x>=0.5 :
    print("Fail")
else :
    print("Enter the Good Score")
