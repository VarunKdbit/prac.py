# How to reverse a number using logic of extraction of digits
n = int(input("Enter the number  : "))
rev=0
while n>0 :
    i=n%10
    n=n//10
    rev=rev*10 +i
print("The reversed version of number is :", rev)
