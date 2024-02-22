class Person:
    name = 'Adnan'
    age = 22
    occupation = 'Software Engineer'

    def detail(self):
        # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        print(f"my name {self.name} and {self.occupation}")


p1 = Person()
p1.name = "dawood"
p1.occupation = "driver"
p1.detail()

# easy example of f-string
name = "adnan"
print(f"i am {name}")
