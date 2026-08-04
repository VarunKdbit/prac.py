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