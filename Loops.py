#1. Write a program to print  “Bright IT Career”  ten times using for loop
for i in range(1,11):
    print("Bright IT Career")
#2. Write a java program to print 1 to 20 numbers using the while loop.
n=1
while(n<=20):
    print(n)
    n=n+1
#3. Program to equal operator and not equal operators
a= 10
b= 20
print(a==b)
print(a!=b)
#4. Write a program to print the odd and even numbers. 
a = list(map(int,input().split()))
even = []
odd = []
for i in a:
    if (i % 2 ==0):
        even.append(i)
    else:
        odd.append(i) 
print("Even Numbers:" ,even)
print("Odd Numbers:" ,odd)
#5. Write a program to print largest number among three numbers.
a= list(map(int,input().split()))
largest = a[0]
for i in range(3):
    if a[i]>largest:
        largest = a[i]
print("Largest Number:",a[i])
#6. Write a  program to print even number between 10 and 20 using while 
n=10
while (n<=20):
    if(n%2 == 0):
        print(n)
    n=n+1
#7. Write a program to print 1 to 10 using the do-while loop statement. 
n = 1  

while True: 
    print(n)
    n = n + 1
    
    if n > 10:  
        break
#8. Write a program to find Armstrong number or not 
a = int(input())
temp = a
sum = 0
order = len(str(a))
while temp >0:
    digit = temp% 10
    sum += digit ** order 
    temp = temp // 10
if sum == a:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
#9. Write a program to find the prime or not. 
a = int(input())
if a<1 and a % 2==0:
    print("It is not prime")
else:
    for i in range(2,a//2+1):
       if a % i == 0:
          print("It is not prime")
          break
    else:
        print("It is prime")
#10.  Write a program to palindrome or not. 
num = int(input())
temp = num
rev = 0
while (temp > 0):
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
if rev == num:
    print("It is palindrome")
else:
    print("It is not palindrome")
#11. Program to check whether a number is EVEN or ODD using switch 
num = int(input("Enter a number: "))

match num % 2:
    case 0:
        print("Even number")
    case 1:
        print("Odd number")
#12. Print gender (Male/Female) program according to given M/F using switch 
ch = (input("Enter a Gender: "))

match ch:
    case 'M':
        print("Male")
    case 'F':
        print("Female")
