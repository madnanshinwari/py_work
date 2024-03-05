class Shape:
    def area(self):
        print("calculating the area...")


class cricle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self, ):
        print("calculating area of the cricle ")
        super().area()
        return 3.14 * self.radius * self.redius


obj = Shape()
obj.area()
