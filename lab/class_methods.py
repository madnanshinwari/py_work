class Students:
    std_name = 'Fahad'

    def showOuput(self):
        print(f"the name of student is : {self.std_name}")

    @classmethod  # class decorator
    # instead of cls you write any thing this is referance to the class
    def changeName(cls, new_std_name):
        cls.std_name = new_std_name    # cls instance is the class


std = Students()
std.changeName("dawood")
std.showOuput()
print(Students.std_name)

# ========== dir() method ===========
x = [1, 2, 3]
# show all method and attributes which are show in this varibale
print(dir(x))

# =========== __dict()__  method =========


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("John", 30)
print(p.__dict__)  # attributes can return in thr form of dictionary.

# =========== help() =========

help(p)  # show the help documentation of the objection
