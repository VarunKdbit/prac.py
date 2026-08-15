#program 1
class Student :
    college = "DBIT"

    def __init__(self,name,marks) :
        self.name = name
        self.marks = marks 

    def welcome(self) :
        print("welcome",self.name)

    def get_marks(self) :
        return self.marks

s1 = Student("varun",67)
s1.welcome()
print(s1.get_marks())
