def avg(a, b):
    avg = a+b/2
    print("the avarage is :", avg)


avg(20, 10)

# deafult arguments


def fullname(first_name, middle_name='Adnan', last_name="khan"):
    print(first_name, middle_name, last_name)


fullname("Muhammad")


"""def name(fname, mname="Jhon", lname="Whatson"):
    print("Hello,", fname, mname, lname)


name("Amy")"""

# keyword arguments


def fullName(fName, lName):
    print(fName, lName)


fullName("Adnan", "khan")

# arbitrary arguments


def fruitsName(*name):
    print(type(name))
    print('fruits names:', name[0], name[1], name[2])


fruitsName("banana", "apple", "orange", "mango")


# keyword arbitrary arguments
# show the values in thor form of dictionary
def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="ali ", lname="khan", fname="Ahmad ")

# return keyword


def add(a, b):
    return a+b

    # print("the sum of a & b is :", a+b)
add(7, 8)
