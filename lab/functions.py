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

#


def fruitsName(*name):
    print(type(name))
    print('fruits names:', name[0], name[1], name[2])


fruitsName("banana", "apple", "orange", "mango")
