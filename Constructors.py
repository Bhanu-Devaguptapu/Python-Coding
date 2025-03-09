#1. Write a class with a default constructor, one argument constructor and two argument 
constructors. Instantiate the class to call all the constructors of that class from a main 
class 
class Example:
    # Default Constructor
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor Called")
        elif arg2 is None:
            print(f"One-Argument Constructor Called: arg1 = {arg1}")
        else:
            print(f"Two-Argument Constructor Called: arg1 = {arg1}, arg2 = {arg2}")

# Main class to instantiate the class and call all constructors
if __name__ == "__main__":
    obj1 = Example()         # Calls default constructor
    obj2 = Example(10)       # Calls one-argument constructor
    obj3 = Example(10, 20)   # Calls two-argument constructor
#2. Call the constructors(both default and argument constructors) of super class from a child class
class Parent:
    def __init__(self, arg=None):
        if arg is None:
            print("Parent Default Constructor Called")
        else:
            print(f"Parent Argument Constructor Called: arg = {arg}")

class Child(Parent):
    def __init__(self, arg=None):
        if arg is None:
            super().__init__()  # Calls Parent's Default Constructor
            print("Child Default Constructor Called")
        else:
            super().__init__(arg)  # Calls Parent's Argument Constructor
            print(f"Child Argument Constructor Called: arg = {arg}")

# Main Execution
if __name__ == "__main__":
    obj1 = Child()       # Calls Parent's default & Child's default constructor
    obj2 = Child(10)     # Calls Parent's argument constructor & Child's argument constructor
#3. Apply private, public, protected and default access modifiers to the constructor 
class AccessModifiers:
    def __init__(self):  # Public Constructor
        print("Public Constructor Called")

    def _protected_constructor(self):  # Protected Constructor (not enforced but indicated)
        print("Protected Constructor Called")

    def __private_constructor(self):  # Private Constructor (name-mangled)
        print("Private Constructor Called")

# Main Execution
if __name__ == "__main__":
    obj = AccessModifiers()  # Calls Public Constructor
    obj._protected_constructor()  # Can be accessed (not recommended)
    
    # obj.__private_constructor()  # ❌ Cannot be accessed directly (will raise an error)
    obj._AccessModifiers__private_constructor()  # ✅ Access via name mangling (not recommended)
#4. Write a program which illustrates the concept of attributes of a constructor.
class ConstructorAttributes:
    def __init__(self, name, age):
        self.name = name  # Instance Attribute
        self.age = age    # Instance Attribute
        print("Constructor Called")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Main Execution
if __name__ == "__main__":
    obj = ConstructorAttributes("Bhanu", 20)  # Calls Constructor
    obj.display()  # Displays attributes assigned in the constructor
