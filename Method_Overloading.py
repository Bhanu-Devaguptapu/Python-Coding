#1.1. Write two methods with the same name but different number of parameters of same type and call the methods  
class Example:
    # Using default arguments to simulate method overloading
    def display(self, a=None, b=None):
        if a is None and b is None:
            print("No parameters passed")
        elif b is None:
            print(f"One parameter passed: {a}")
        else:
            print(f"Two parameters passed: {a}, {b}")

# Main Execution
if __name__ == "__main__":
    obj = Example()
    obj.display()       # Calls method with no parameters
    obj.display(10)     # Calls method with one parameter
    obj.display(10, 20) # Calls method with two parameters

#2. Write two methods with the same name but different number of parameters of different data type and call the methods  
  class Example:
    # Using `isinstance()` to handle different types
    def display(self, param):
        if isinstance(param, int):
            print(f"Integer parameter: {param}")
        elif isinstance(param, str):
            print(f"String parameter: {param}")
        else:
            print(f"Other type parameter: {param}")

# Main Execution
if __name__ == "__main__":
    obj = Example()
    obj.display(10)        # Calls method with int
    obj.display("Bhanu")   # Calls method with string
    obj.display(10.5)      # Calls method with float

#3. Write two methods with the same name and same number of parameters of same type 
class Example:
    def display(self, a, b):
        print(f"First method: {a} and {b}")

    # This method overrides the previous one
    def display(self, x, y):
        print(f"Second method: {x} and {y}")

# Main Execution
if __name__ == "__main__":
    obj = Example()
    obj.display(10, 20)  # Calls the latest `display()` method (overrides the first one)
