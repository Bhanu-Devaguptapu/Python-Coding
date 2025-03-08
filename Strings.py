#1. Different ways creating a string.
s1 = 'Hello World!' # using single ''
s2 = "Hello World"  # using double " "
s3 = str(100)  # converts interger into strings
name = "World"
s4 = "Hello {}!".format(name)# by using format method
List = ["Animals", "are","good","Friends"]
s5 = " ".join(List) #by using join method
print(s1,s2,s3,s4,s5,sep = "\n")
#2. Concatenating two strings using + operator.
s1 = 'Hello World!'
s2 = 'I am a student'
print(s1 +" "+ s2)
#3. Finding the length of the string
s1 = 'Hello World!'
print(len(s1))
#4. Extract a string using Substring 
string = input("Enter the String:")
sub = string[-5:]
print(sub)
#5. Searching in strings using index()
string = input("Enter the String:")
input = input("Enter the char to be searched:")
sub = string.index(input)
print(sub)
#6. Matching a String Against a Regular Expression With matches() 
import re
s1 = "Hello World!"
s2 = "Hello"
m = re.match(s2,s1)
if m:
    print("It is matched at", m.group())
else:
    print("It is not matched")
#7. Comparing strings  
def strcmp(s1, s2):
    if s1 == s2:
        return 0
    elif s1 < s2:
        return -1
    else:
        return 1

s1 = input("Enter first string:")
s2 = input("Enter second string:")
print(strcmp(s1, s2))
#8.startsWith(), endsWith() and compareTo()
s1 = "Hello World!"
s2 = "I am Coder!"
print(s1.startswith("Hello"))
print(s2.endswith("@"))
def compareTo(s1, s2):
    if s1 == s2:
        return 0
    elif s1 < s2:
        return -1
    else:
        return 1

print(compareTo(s1, s2))
#9. Trimming strings with strip() 
s1 = input("Enter the string:")
print(s1.strip())
#10. Replacing characters in strings with replace() 
s1 = input("Enter the string:")
ip= input("Enter word to be replaced:")
output= input("Enter the word to place:")
print(s1.replace(ip,output))
#11. Splitting strings with split() 
s1 = input("Enter the string:")
ip= input("Enter the char where string to be split:")
print(s1.split(ip))
#12.num = int(input("Enter int value:"))
string_num = str(num)
print(string_num)  
print(type(string_num))
#13. Converting to uppercase and lowercase 
s1 = input("Enter the string:")
print("LowerCase:",s1.lower())
print("UpperCase:",s1.upper())
