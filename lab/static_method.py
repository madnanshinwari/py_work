class Math:
    @staticmethod  # use static method decorator
    def add(a, b):
        return a+b


result = Math.add(5, 5)
print(result)
