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

#recursive a^n

def fun(a,n,m) :
    if n==1 :
        return m
    return fun(a,n-1,m*a) 


n=int(input("enter the power n :"))
m=1
a=int(input("enter the number to be performed :"))

print(fun(a,n,m))

