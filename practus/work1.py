class Employee :

    def __init__(self,role,department,salary) :
        self.role = role
        self.department = department 
        self.salary = salary
        
    def show_details(self) :
        print("ROLE :",self.role)
        print("DEPARTMENT :",self.department)
        print("SALARY :",self.salary)

emp1 = Employee("Software Developer","AIML",80000)
emp1.show_details()

