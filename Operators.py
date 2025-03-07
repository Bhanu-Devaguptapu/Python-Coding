#1. Write a function for arithmetic operators(+,-,*,/)
a= int(input())
b = int(input())
def add():
    print(a+b)
def subtract():
    print(a-b)
def product():
    print(a * b)
def divide():
    print(a / b)
add()
subtract()
product()
divide()
#2. Write a method for increment and decrement operators(++, --).
def increment():
    sum = 10
    for i in range(1,5):
        sum += i
    print(sum)
increment()
def decrement():
    sum = 10
    for j in range(1,5):
        sum -= j
    print(sum)
decrement()  
#3. Write a program to find the two numbers equal or not.
a = int(input())
b = int(input())
if(a==b):
    print("Both are equal")
else:
    print("Bot are not equal")
#4. Program for relational operators (<,<==, >, >==)
a = 10
b = 20
print(a<b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)
#5.  Print the smaller and larger number.
a = int(input())
b = int(input())
if (a>b):
    print("a is larger")
    print("b is smaller")
if( a<b):
    print("a is smaller")
    print("b is larger")

