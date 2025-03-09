class A:
    def __init__(self):
        self.data = "Class A Data"
    def fun1(self):
        print("This is class A")
    def fun2 (self):
        print("This is Python languag")
    def display(self):
        print("Super Class")
class B(A):
    def __init__(self):
        super().__init__()  # Inherit A's constructor
        self.data = "Class B Data"
    def fun3(self):
        print("This is class B")
    def fun4(self):
        print("This is Python language")
    def display(self):
        print("Sub Class1")
class C(B):
    def __init__(self):
        super().__init__()  # Inherit B's constructor
        self.data = "Class C Data"
    def fun5(self):
        print("This is class C")
    def fun6(self):
        print("This is Python language")
    def display(self):
        print("Sub Class2")
if __name__ == "__main__":
    objA = A()
    objB = B()
    objC = C()
#Class A methods
objA.display()
objA.fun1()
objA.fun2()
#Class B methods
objB.display()
objB.fun3()
objB.fun4()
#Class C methods
objC.display()
objC.fun5()
objC.fun6()
#Creating reference for B and C classes for over ridden method
print("\nRuntime Polymorphism (Overridden Method):")
refB = B()
refC = C()

refB.display()
refC.display()

#Runtime polymorphism for data members
print("\nRuntime Polymorphism (Data Members):")
ref1 = A()  # Superclass reference
ref2 = B()  # Reference to B object
ref3 = C()  # Reference to C object

print(ref1.data)  # Class A Data
print(ref2.data)  # Class B Data
print(ref3.data)  
