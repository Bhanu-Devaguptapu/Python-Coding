#1. Define a static variable and access that through a class 
class Student:
    stu_name = "Devaguptapu Bhanu Sri"
print(Student.stu_name)
obj = Student()
#2.Define a static variable and access that through a instance 
class Student:
    stu_name = "Devaguptapu Bhanu Sri"
obj = Student()
print(obj.stu_name)
#3. Define a static variable and change within the instance.
class Student:
    stu_name = "Devaguptapu Bhanu Sri"
obj = Student()
obj.stu_name = "Bhagath"
print("Instance Variable:",obj.stu_name)
print("Class Variable:",Student.stu_name)
#4. Define a static variable and change within the class.
class Student:
    stu_name = "Devaguptapu Bhanu Sri"
obj = Student()
print("Instance Variable:",obj.stu_name)
Student.stu_name = "Bhagath"
print("Class Variable:",Student.stu_name)
