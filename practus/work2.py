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
