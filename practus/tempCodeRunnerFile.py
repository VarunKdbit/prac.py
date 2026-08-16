class Student :
    name = "Anonymous"

    @classmethod
    def change_name(cls,name) :
        cls.name = name

s1 = Student
s1.change_name("DBIT")
print(Student.name)
print(s1.name)