def pr(n):
    
    if(n==0):
        return
    print(n)
    pr(n-1)
n=int(input("enter the number : "))
print(pr(n))
