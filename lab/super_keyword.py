class Parent_class:
    def parent_method(self):
        print("this is a parent class")


class child_class(Parent_class):
    def child_method(self):
        print("this is a child class")
        # super keyword is which call the parent class method from the child class
        super().parent_method()


child_obj = child_class()
child_obj.child_method()
