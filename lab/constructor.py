class Person:
    def __init__(self, n, a):
        # print("i'm constructor")
        self.name = n
        self.age = a

    def output(self):
        print(f"my name is {self.name} and my age is {self.age}")


# one method to access value
p1 = Person("Adnan", 22)
print(f"I'm {p1.name} and my age is {p1.age}")

# another method to access the values to create a function and call it
p2 = Person("Dawood", 23)
p2.output()
