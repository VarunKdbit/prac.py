def c(n):
    if n<=1:
        return n
    else :
        return n+c(n-1)
n=int(input("enter the num : "))

print(c(n))