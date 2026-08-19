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
