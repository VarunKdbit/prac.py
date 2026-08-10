#program 1:

movies=[]
movies.append(input("enter your 1st favorite movie "))
movies.append(input("enter your 2nd favorite movie "))
movies.append(input("enter your 3rd favorite movie "))
print(movies)

#program 2:

list=[1,2,3,2,1]
cl=list.copy()
cl.reverse()
if(list==cl):
    print("palindrome list ")
else :
    print("not a palindrome list")

#program 3 :

marks_sheet = {
    "NAME" : "VARUN K",
    "GRADE" : "A",
    "MARKS" : {
        "PHYSICS" : 67,
        "CHEMISTRY" : 90,
        "HISTORY" : 97,
        "BIOLOGY" : 83,
        "COMPUTER SCIENCE" : 69
    },
    "GRADE" : "A",
}
print(marks_sheet)

#program 4 :

data ={
    "NAME" : input("enter the name "),
    "MARKS" : {
        "m1" : input("enter the sub1 marks "),
        "m2" : input("enter the sub2 marks "),
    },
    "GRADE" : input("enter the grade obtained ")
}
print(data) 
data["MARKS"]["m2"] = 91
print(data)
data["YEAR"] = 2026
print(data)
print(data.keys())
print(data.values())
print(data.items())

#program 4:

nums=[13,45,6,4,15,7]
n=len(nums)
t=10
for i in range (0,n):
    for j in range (i,n) :
        if nums[i]+nums[j]==t :
            print(i,j)

#program 5

text = input("enter the text")
u=0
l=0
for i in text:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("count of upper char in the text is :",u)
print("count of lower char in the text is :",l)

#program 6

n=int(input("enter the number:"))
a=0
b=1
print("fibonacci series for the entered number is : ")
print(a)
print(b)
for i in range(n-2):
    c=a+b
    print(c)
    a=b
    b=c
print("end of program ")

# PROGRAM 7

#method 1
num=int(input("enter the number : "))
if(num<2):
    print("not prime")
    exit()
for i in range (2,num):
    if(num%i==0):
        print("not prime")
        exit()
print("prime")

#method 2
n=int(input("enter the number : "))
prime =True
if n<2 :
    prime = False
else:
    for i in range(2,n):
        if(n%i==0):
            prime= False
            break
if prime:
    print("Prime")
else :
    print("NotPrime")
    
#method 3
n=int(input("enter the number :"))
if(n<2):
    print("not prime")
else :
    for i in range (2,n):
        if(n%i==0):
            print("not prime")
            break
    else:
        print("prime")

#program 8

n=int(input("enter the number : "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial of given number is :",fact)

#program 9

def even(n):
    if(n<=1):
        return 
    if(n%2==0):
        print(n)
    even(n-1)
#recursion factorial 

def fact(n):
    if n==0 or n==1 :
        return 1
    else :
        return n*fact(n-1)
    
n=int(input("enter the value of n : "))
print(fact(n))

#recursive sum of n numbers

def c(n):
    if n<=1:
        return n
    else :
        return n+c(n-1)
n=int(input("enter the num : "))

print(c(n))



