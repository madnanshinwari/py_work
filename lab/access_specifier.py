# all variable and methods by default public

class Person:
    # constructor
    def __init__(self, name, gender):
        self.name = name  # public variable
        self.gender = gender  # public variable

    def showOutput(self):
        print(f"Name:{self.name} and Gender: {self.gender}")


p1 = Person("Adnan", "Male")
p1.showOutput()
print(p1.gender)
print(p1.name)


# private access specifier
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def outPut(self):
        print(f"Roll no :{self.roll_no}  Name: {self.name}")


std1 = Student(47, "Dawood")
std1.outPut()
