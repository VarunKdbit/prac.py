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
