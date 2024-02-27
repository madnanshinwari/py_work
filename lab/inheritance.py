class Vehicle:
    def __init__(self, model, name):
        self.model = model
        self.name = name

    def showDetails(self):
        print(f"the model is: {self.model} and name is: {self.name}")

# derived class


class Honda(Vehicle):
    def hello(self):
        print("Hi! i'm a inherit class  ")


v1 = Vehicle(123, "Honda")
v1.showDetails()
# v2 = Vehicle(456, "Tesla")
# v2.showDetails()
v3 = Honda(567, "toyota")
v3.showDetails()
v3.hello()


# v2.hello()
