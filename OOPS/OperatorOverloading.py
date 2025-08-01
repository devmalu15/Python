class Student:
    def __init__(self, marks):
        self.marks = marks

    def __add__(self, other):
        sum = self.marks + other.marks
        obj = Student(sum)
        return obj
    

s1 = Student(100)
s2 = Student(200)
s3 = s1 + s2
print(s3.marks)