
# ------ getter --------
class Myclass:
    def __init__(self, value):
        self._value = value

    @property  # it's user of to return value of  specific property.
    def value(self):
        return self._value


obj = Myclass(15)
obj.value
print(f"the getter value : {obj.value}")

# --------- setter -------


class Myclass:
    def __init__(self, value):
        self._value = value

    @property  # it's user of to return value of  specific property.
    def value(self):
        return self._value

    @value.setter  # they can set or add value
    def value(self, new_value):
        self._value = new_value


obj = Myclass(15)
obj.value = 20

print(f"the setter value : {obj.value}")
