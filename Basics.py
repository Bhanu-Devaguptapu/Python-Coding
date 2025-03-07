#1. Write a program to print your name. 
print ("Bhanu Sri Devaguptapu")
#2. Write a program for a Single line comment and multi-line comments 
# Single line Comment
''' Multi Line Comments are easy 
and help to understand the code '''
#3.  Define variables for different Data Types int, Boolean, char, float, double and print on the Console. 
a = 10
print(a, type(a))
b = 'c '
print(b, type(b))
c = True 
print(c, type(c))
d = 50.25
print(d, type(d))
e = 27.987654
print(e, type(e))
#4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables
a = 5
def f():
    print('Inside f() : ', a)
def g():
    a = 2
    print('Inside g() : ', a) 
def h():
    global a
    a = 4      
    print('Inside h() : ', a)  
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

