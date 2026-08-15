class Student :
    
    def __init__(self,name,marks) :
        self.name = name 
        self.marks =marks


    @staticmethod
    def hello() :
        print("hello")

    def avg(self) :
        sum=0
        for i in self.marks :
            sum+=i
        avg=sum/4
        print("Hi",self.name,"your avg marks is :",avg)


s1 =Student("varun",[6.7,5.9,6.0,8.4])
s1.hello()
s1.avg()

