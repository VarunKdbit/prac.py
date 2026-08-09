num=int(input("enter the number : "))
if(num<2):
    print("not prime")
    exit()
for i in range (2,num):
    if(num%i==0):
        print("not prime")
        exit()
print("prime")