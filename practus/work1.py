class Employee :

    def __init__(self,role,department,salary) :
        self.role = role
        self.department = department 
        self.salary = salary
        
    def show_details(self) :
        print("ROLE :",self.role)
        print("DEPARTMENT :",self.department)
        print("SALARY :",self.salary)

class Engineer(Employee) :

    def __init__(self,name,age,role,dept,salary) :
        self.rol =role
        self.dept =dept
        self.slry =salary
        self.name = name
        self.age = age
        super().__init__(self.rol,self.dept,self.slry)

emp1 = Engineer("VARUN K",21,"PYTHON BACKEND","AIML","3700000")
emp1.show_details()




