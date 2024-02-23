def greet():
    print("Good Morning")


def my_decorator(ftn):
    def check():
        print("before decorator")
        ftn()
        print("after decorator")
    return check()


@my_decorator
def greet():
    print("Good Morning")


greet()
