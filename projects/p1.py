print("Welcome program begins!!!")
m1=int(input("enter the number of marks scored in sub 1"))
m2=int(input("enter the number of marks scored in sub 2"))
m3=int(input("enter the number of marks scored in sub 3"))
m4=int(input("enter the number of marks scored in sub 4"))
m5=int(input("enter the number of marks scored in sub 5"))
m6=int(input("enter the number of marks scored in sub 6"))
total=m1+m2+m3+m4+m5+m6
perc=(total/600)*100
print("the percentage scored by student is :",perc )
if(perc>90):
    print("A+")
elif(perc>80):
    print("A")
elif(perc>75):
    print("B+")
elif(perc>60):
    print("B")
elif(perc>35):
    print("PASS")
else :
    print("FAIL")
print("End of program")


