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

#program 2
class Student :
    
    def __init__(self,name,marks) :
        self.name = name 
        self.marks =marks

    def avg(self) :
        sum=0
        for i in self.marks :
            sum+=i
        avg=sum/4
        print("Hi",self.name,"your avg marks is :",avg)

s1 =Student("varun",[6.7,5.9,6.0,8.4])
s1.avg()

#program 3
