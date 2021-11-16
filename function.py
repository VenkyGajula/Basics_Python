def add(a,b) :
  sum=a+b
  return sum
a=int(input("Enter the value of a = "))
b=int(input("Enter the value of b ="))
#res=add(a,b)
print("Result =",add(a,b))

print("****Example of function****")
x=10
def print_Lyrics() :
    print("My name is Gajula Venkateshwarlu")
    print("Iam from Andhra Pradesh")
    print("My qualification is Master of Computer Applications")
print("********")
x=x+5
print(x)
print_Lyrics()
print("**************")
x=float(input("Enter the your Score"))
def greet(x) :
    if x>=10 :
        print("OutStanding")
    elif x>=9 :
        print("A")
    elif x>=8 :
        print("B")
    elif x>=7 :
        print("C")
    elif x>=6 :
        print("D")
    elif x>=5 :
        print("Fail")
    else :
        print("Enter the correct Score")
greet(x)
print("*****Return Keyword****")
def str() :
    return "Hello"
print(str(),"Venky")
print(str(),"Madhu")
print("***********")

def sub(lang) :
    if lang == 'es' :
        return 'English'
    elif lang == 'ms' :
        return "Maths"
    elif lang == 'cs' :
        return "computer Applications"
    else :
        return "Enter the correct language"
print(sub('ms'),"Achari")
print(sub('en'),"Venky")
print(sub('cs'),"Ravi")
print("******")
h=int(input("Enter the Hours"))
r=int(input("Enter the rate"))
def comp(h,r) :
    pay=(h-5)*r+5*15
    return pay
print("Enter Hour = ",h)
print("Enter rate = ",r)
print("Pay = ",comp(h,r))
