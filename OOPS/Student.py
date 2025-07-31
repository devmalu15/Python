class Student:    #class decralaration

    college = "GLA University, Mathura"         #class/static variable(same for all the objects)

    def __init__(self, name: str, age: int):    #cunstructor
        self.name = name                        #instance variable(different for every object)
        self.age = age                          #instance variable(different for every object)

    def changeAge(self, newAge: int) -> None:    #method
        self.age = newAge


    def __str__(self) -> str:                    #dunder method
        return f"{self.name}, {self.age}"
        

student1: Student = Student("Dev", 20)           #creating object
student2: Student = Student("abc", 21)
#print(f"name = {student1.name} and age = {student1.age}")
student1.changeAge(21)
#print(f"name = {student1.name} and age = {student1.age}")
#print(student1)

print(f"{student1.name} {student1.age} {student1.college}")
print(f"{student2.name} {student2.age} {student2.college}")

Student.college = "Passout"                       #changing class variable

print(f"{student1.name} {student1.age} {student1.college}")
print(f"{student2.name} {student2.age} {student2.college}")



