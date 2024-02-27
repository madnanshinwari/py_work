class Math:
    @staticmethod  # use static method decorator
    def add(a, b):
        return a+b


# the method can be call itself not using the any instance or object of the class.
result = Math.add(5, 5)
print(result)
