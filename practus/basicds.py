# How to reverse a number using logic of extraction of digits
n = int(input("Enter the number  : "))
rev=0
while n>0 :
    i=n%10
    n=n//10
    rev=rev*10 +i
print("The reversed version of number is :", rev)

#Check number is palindrome or not 
x=int(input("Enter the number : "))
n=x
nc=0
while n>0 : 
    i=n%10 
    n=n//10
    nc=nc*10 + i
if nc == x :
    print("Entered number is palindrome")
else :
    print("Entered number is not a palindrome")

#How to check whether the number is armstrong or not
# Method 1:
n=int(input("Enter the number:"))
num=n
count=0
while num >0:
    count+=1
    num=num//10
na=n
arm=0
while na>0 :
    i=na%10
    arm+=i**count
    na=na//10
if(arm==n) :
    print("armstrong number")
else :
    print("not an armstrong number")

# Method2:
n=int(input("Enter the number : "))
count=len(str(n))
num=n
arm=0
while num>0 :
    i=num%10
    arm+=i**count
    num=num//10
if arm==n :
    print("Entered number is a Armstrong number")
else :
    print("Entered number is not a Armstrong number")



