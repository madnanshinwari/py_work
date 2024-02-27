# protected : protected can access by itself and subclasses.
# ->the convention of the indicating is the member is protected the prefix the single underscore
class Student:
    def __init__(self):
        self._name = "Adnan"

    def _funName(self):      # protected method
        return "Islamia college "


class Subject(Student):  # inherited class
    pass


obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
