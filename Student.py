class Student:
    major='CSE'
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
s1=Student(1,'Sourav')
print(s1.major)
print(s1.name)
s2=Student(2,'Raj')
print(s2.name)
print(Student.major)
