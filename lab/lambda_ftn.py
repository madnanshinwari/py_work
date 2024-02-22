# use lambda keyword when write a function


# def double(n):
#     return n * 2

# def double(x): return x * 2
def double(x): return x * 2


print('this is a lambda function ', double(5))


def cube(x): return x*x*x


print(cube(5))

# call one function to inside another function


def both_ftn(ftn, value):
    return 6 + ftn(value)


print("value of both function is : ", both_ftn(cube, 78))
