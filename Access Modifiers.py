#1. Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the private method in main method. Create a sub class and try to access the private fields and methods from sub class.
class A:
    def __init__(self):
        self.__private_field = "This is a private field"

    def __private_method(self):
        print("This is a private method of Class A")

    def access_private_method(self):
        print("Accessing private method inside class A:")
        self.__private_method()  # Private method can be accessed within the same class

class B(A):
    def access_parent_private(self):
        try:
            print(self.__private_field)  # Trying to access private field
        except AttributeError:
            print("Cannot access private field directly from subclass")

        try:
            self.__private_method()  # Trying to access private method
        except AttributeError:
            print("Cannot access private method directly from subclass")

# Main Method
if __name__ == "__main__":
    objA = A()

    # Accessing private field using name mangling
    print("\nAccessing Private Field in Main Method:")
    print(objA._A__private_field)  # Works because of name mangling

    # Calling private method using name mangling
    print("\nCalling Private Method in Main Method:")
    objA._A__private_method()  # Works because of name mangling

    # Calling private method from within the class
    objA.access_private_method()

    # Creating an object of subclass B
    objB = B()

    print("\nTrying to Access Private Members from Subclass:")
    objB.access_parent_private() 
  #2. 2. Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package.  
#Also, Access the PROTECTED fields and methods from child class located in a different package 
#Access the PROTECTED fields and methods from any class in different package 
# Class with Protected Fields and Methods
class Parent:
    def __init__(self):
        self._protected_var = "This is a PROTECTED variable"

    def _protected_method(self):
        print("This is a PROTECTED method")

# Accessing Protected Members from Another Class in the Same Module
class AnotherClass:
    def access_protected(self):
        obj = Parent()
        print("\nAccessing Protected Members from Another Class:")
        print(obj._protected_var)  # Allowed (Protected)
        obj._protected_method()  # Allowed (Protected)

# Accessing Protected Members from a Child Class (Simulating a Different Module)
class Child(Parent):
    def access_protected_in_child(self):
        print("\nAccessing Protected Members from Child Class:")
        print(self._protected_var)  # Allowed (Protected)
        self._protected_method()  # Allowed (Protected)

# Accessing Protected Members from an Unrelated Class in a Different Module
class Unrelated:
    def access_protected_unrelated(self):
        obj = Parent()
        print("\nAccessing Protected Members from an Unrelated Class (Not Recommended):")
        print(obj._protected_var)  # Allowed but Not Recommended
        obj._protected_method()  # Allowed but Not Recommended

# Main Method
if __name__ == "__main__":
    obj1 = Parent()
    print("\nAccessing Protected Members from Main Method:")
    print(obj1._protected_var)  # Direct access
    obj1._protected_method()  # Direct access

    obj2 = AnotherClass()
    obj2.access_protected()  # Accessing from another class

    obj3 = Child()
    obj3.access_protected_in_child()  # Accessing from subclass

    obj4 = Unrelated()
    obj4.access_protected_unrelated()  # Accessing from an unrelated class


  #3. Create a class with PUBLIC fields and methods.  #Access the public methods and fields from any class in the same package or different package.
# Class with Public Fields and Methods
class Parent:
    def __init__(self):
        self.public_var = "This is a PUBLIC variable"

    def public_method(self):
        print("This is a PUBLIC method")

# Accessing Public Members from Another Class in the Same Module
class AnotherClass:
    def access_public(self):
        obj = Parent()
        print("\nAccessing Public Members from Another Class:")
        print(obj.public_var)  # Accessing public variable
        obj.public_method()  # Accessing public method

# Main Method
if __name__ == "__main__":
    obj1 = Parent()
    print("\nAccessing Public Members from Main Method:")
    print(obj1.public_var)  # Direct access
    obj1.public_method()  # Direct access

    obj2 = AnotherClass()
    obj2.access_public()  # Accessing from another class
  
