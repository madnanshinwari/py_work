
# private access specifier
# show the attributes error in output we access this variable and methods through name mangling
class Student:
    def __init__(self, roll_no, name):
        self.__roll_no = roll_no
        self.__name = name

    def __outPut(self):
        print(f"Roll no :{self.__roll_no}  Name: {self.__name}")


std = Student(47, "Dawood")
std.outPut()
print(std._Student__name)
print(std.__roll_no)
print(std._Student_output())


# name mangling  technique

class Student:
    def __init__(self, roll_no, name):
        self.__roll_no = roll_no
        self.__name = name

    def __outPut(self):
        print(f"Roll no :{self.__roll_no}  Name: {self.__name}")


std = Student(47, "Dawood")
# std.__outPut()
# In name mangling we access the private varible we use the _before the class name
print(std._Student__name)
print(std._Student__roll_no)
