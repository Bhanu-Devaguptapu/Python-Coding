#Create a program to create two class.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}")

class School:
    def __init__(self, school_name):
        self.school_name = school_name

    def show_school(self):
        print(f"School Name: {self.school_name}")

# Main Execution
if __name__ == "__main__":
    student1 = Student("Bhanu", 20)
    school1 = School("Aditya Degree College")

    student1.display()  # Calls method from Student class
    school1.show_school()  # Calls method from School class
#   1.1. Create a constructor and a method for each class
class Student:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def display_student(self):  # Method
        print(f"Student Name: {self.name}, Age: {self.age}")

class School:
    def __init__(self, school_name, location):  # Constructor
        self.school_name = school_name
        self.location = location

    def display_school(self):  # Method
        print(f"School Name: {self.school_name}, Location: {self.location}")

# Main Execution
if __name__ == "__main__":
    student1 = Student("Bhanu", 20)
    school1 = School("Aditya Degree College", "Rajahmundry")

    student1.display_student()  # Calls method from Student class
    school1.display_school()  # Calls method from School class
#1.2. Create a __init__.py for adding all packages
# Student Class
class Student:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def display_student(self):  # Method
        print(f"Student Name: {self.name}, Age: {self.age}")

# School Class
class School:
    def __init__(self, school_name, location):  # Constructor
        self.school_name = school_name
        self.location = location

    def display_school(self):  # Method
        print(f"School Name: {self.school_name}, Location: {self.location}")

# Main Execution
if __name__ == "__main__":
    student1 = Student("Bhanu", 20)
    school1 = School("Aditya Degree College", "Rajahmundry")

    student1.display_student()  # Calling Student class method
    school1.display_school()  # Calling School class method
#1.3 Import the respective packages
# Student Class
class Student:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def display_student(self):  # Method
        print(f"Student Name: {self.name}, Age: {self.age}")

# School Class
class School:
    def __init__(self, school_name, location):  # Constructor
        self.school_name = school_name
        self.location = location

    def display_school(self):  # Method
        print(f"School Name: {self.school_name}, Location: {self.location}")

# Simulating Package Import (Manually Defining a Package)
class MyPackage:
    @staticmethod
    def get_student(name, age):
        return Student(name, age)

    @staticmethod
    def get_school(school_name, location):
        return School(school_name, location)

# Main Execution
if __name__ == "__main__":
    # Creating objects using the simulated package
    student1 = MyPackage.get_student("Bhanu", 20)
    school1 = MyPackage.get_school("Aditya Degree College", "Rajahmundry")

    # Calling methods
    student1.display_student()
    school1.display_school()

# 1.4. Calling each class by creating objects
if __name__ == "__main__":
    # Creating objects using MyPackage (Simulating package import)
    student1 = MyPackage.get_student("Bhanu", 20)
    school1 = MyPackage.get_school("Aditya Degree College", "Rajahmundry")

    # 1.5. Display output by calling methods
    student1.display_student()  # Calls Student class method
    school1.display_school()  # Calls School class method
