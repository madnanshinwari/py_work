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
