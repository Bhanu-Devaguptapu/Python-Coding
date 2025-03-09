#1. Create an abstract class with abstract and non-abstract methods. 
from abc import ABC, abstractmethod

# Abstract Class
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):  # Abstract Method (Must be implemented in subclasses)
        pass

    def non_abstract_method(self):  # Regular Method (Can be used directly)
        print("This is a NON-ABSTRACT method")

# Concrete Subclass (Implements the Abstract Method)
class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("This is an ABSTRACT method implementation")

# Main
if __name__ == "__main__":
    obj = ConcreteClass()
    obj.abstract_method()  # Calls the implemented abstract method
    obj.non_abstract_method()
  #2. 2. Create a sub class for an abstract class. Create an object in the child class for the  abstract class and access the non-abstract methods 
  from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):  # Abstract Method
        pass

    def sleep(self):  # Non-Abstract Method
        print("Animal is sleeping") 

# Subclass of Abstract Class
class Dog(Animal):
    def make_sound(self):  
        print("Dog barks")  

    def access_abstract_class_methods(self):
        print("\nAccessing non-abstract method from abstract class:")
        self.sleep()  # Calling non-abstract method from the abstract class

# Creating an object of the subclass
if __name__ == "__main__":
    dog = Dog()
    dog.access_abstract_class_methods()
  ##3. Create an instance for the child class in child class and call abstract methods 
  from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):  # Abstract Method
        pass

# Subclass of Abstract Class
class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

    def create_instance_and_call(self):
        print("\nCreating instance of Dog inside Dog class:")
        obj = Dog()  # Creating an instance of the child class inside itself
        obj.make_sound()  # Calling the abstract method implementation

# Main Execution
if __name__ == "__main__":
    dog = Dog()  
    dog.create_instance_and_call()  
