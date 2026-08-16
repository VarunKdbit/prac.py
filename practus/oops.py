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

#program 3 (with using decorator )
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
        print(self.name,"your avg marks is :",avg)


s1 =Student("varun",[6.7,5.9,6.0,8.4])
s1.hello()
s1.avg()

#program 4
class Bank :

    def __init__(self,name,acc_no,bal) :
        self.name = name
        self.account_number = acc_no
        self.balance = bal

    def debit(self,amount) :
        self.balance-=amount
        print("Hi",self.name,"Rs.",amount,"was debited to your account")
        print("available net total balance is",self.check_balance())

    def credit(self,amount) :
        self.balance+=amount
        print("Hi",self.name,"Rs.",amount,"was credited to your account")
        print("available net total balance is",self.check_balance())

    def check_balance(self):
        return self.balance

#INHERITANCE

#program 5(single level inheritance)
class Car :

    @staticmethod 
    def start() :
        print("Car has started.....")

    @staticmethod
    def stop() :
        print("Car has stopped")

    
class Toyota(Car) :

    def __init__(self,name,model) :
        self.name = name
        self.model = model

car1 = Toyota("Fortuner",2017)
print(car1.name,car1.model)
car1.start()
car1.stop()
car2 = Toyota("Vellfire",2023)
print(car2.name,car2.model)
car2.start()
car2.stop()

# multi-level inheritance

class Animal :
    @staticmethod
    def eat() :
        print("eats")

class Dog(Animal) :
    
    def bark(self) :
        print(self.name,"barks")

class Pup(Dog) :

    def __init__(self,name) :
        self.name = name

    def play(self) :
        print(self.name,"plays")

D1 = Pup("charlie")
D1.bark()
D1.eat()
D1.play()

#program 6 (multiple inheritance)
class Soulreaper() :
    @staticmethod
    def spiritualpressure() :
        print("Reitsu")

    def zanpakto(self) :
        print(self.name,"has a shikai")
class Hollow() :
    @staticmethod
    def regeneration() :
        print("can regenerate")

    def Mask(self):
        print(self.name,"has Hollow mask abilities")
class Visords(Soulreaper,Hollow) :

    def __init__(self,name) :
        self.name = name 

p1 = Visords("Shinji Hirako")
p1.zanpakto()
p1.Mask()

#super() method 
# it is used to access method of parent class
class Car :

    def ty(self,type) :
        self.type = type 
        
    @staticmethod
    def start() :
        print("car starts")

    @staticmethod
    def stop() :
        print("car stops")

class Toyota(Car) :
    def __init__(self,name,type) :
        super().ty(type)
        self.name=name

car1 = Toyota("Fortuner","Petrol")
print(car1.name)
print(car1.type)


#class method 
#it bounds to  the class rather than a specific object and it can access or modify class attributes
class Student :
    name = "Anonymous"

    @classmethod
    def change_name(cls,name) :
        cls.name = name

s1 = Student
s1.change_name("DBIT")
print(Student.name)
print(s1.name)

#property method
# it is used to access methods like a attribute
class Result :

    def __init__(self,AI,CN,LLM,ADA) :
        self.AI = AI
        self.CN = CN
        self.LLM = LLM
        self.ADA = ADA

    @property 
    def percentage(self) :
        print(str(((self.AI + self.CN + self.LLM + self.ADA)/400)*100 ) +"%" )

s1 = Result(75,70,80,70)
s1.percentage
