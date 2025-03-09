#1. Write a program to generate Arithmetic Exception without exception handling 
# Division by zero will cause an Arithmetic Exception
num = 10
result = num / 0  
print("This line will not execute")

#2. Handle the Arithmetic exception using try-catch block 
try:
    num = 10
    result = num / 0  # Causes ZeroDivisionError
except ZeroDivisionError:
    print("Arithmetic Exception: Division by zero is not allowed!")

#3. Write a method which throws exception, Call that method in main class without try block 
  def divide():
    raise ZeroDivisionError("This is a ZeroDivisionError")  # Throwing an exception

# Calling method without handling exception
divide() 

#4. Write a program with multiple catch blocks 
try:
    num = int(input("Enter a number: "))
    result = 10 / num  # Can cause ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
except Exception as e:
    print("General Exception:", e)

#5. Write a program to throw exception with your own message 
  def check_number(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed!")  # Custom Exception
    print("Valid number:", n)

check_number(-5)  

#6. Write a program to create your own exception 
# Custom Exception Class
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)

# Raising Custom Exception
def check_age(age):
    if age < 18:
        raise MyException("Age must be 18 or above!")
    print("Access granted")

check_age(15)  

#7. Write a program with finally block 
try:
    print("Trying to divide...")
    result = 10 / 0  # Causes ZeroDivisionError
except ZeroDivisionError:
    print("Exception caught: Division by zero")
finally:
    print("Finally block executed (Cleanup code)")

#8. Write a program to generate Arithmetic Exception 
  # Arithmetic Exception (Division by zero)
num = 10 / 0 

#9. Write a program to generate FileNotFoundException 
# Trying to open a file that doesn't exist
with open("nonexistent_file.txt", "r") as file:  
    content = file.read()

#10. Write a program to generate ClassNotFoundException 
  try:
    import nonexistent_module  
except ImportError:
    print("ClassNotFoundException: Module not found")

#11. Write a program to generate IOException 
  try:
    with open("readonly_file.txt", "w") as file:  # Trying to write in a read-only file
        file.write("Hello")
except OSError:
    print("IOException: Error in file operation")

#12. Write a program to generate NoSuchFieldException
class Example:
    def __init__(self):
        self.name = "Bhanu"

obj = Example()
print(obj.age)  
