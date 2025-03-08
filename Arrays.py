#1. Write a function to add integer values of an array
def add(n):
    return list(map(int, input().split()))  
n = int(input("Enter the number: "))  
array = add(n)  
print("Array:", array)
#2. Write a function to calculate the average value of an array of integers.
arr= list(map(int,input().split()))
def avg(arr):
    sum =0
    for i in arr:
        sum += i
    return sum/len(arr)   

average = avg(arr)  
print("Average:", average)
#3. Write a program to find the index of an array element.
arr= list(map(int,input().split()))
n = int(input("Enter the element:"))
for i in range(0,len(arr)):
    if arr[i] == n:
        print("Index Number is: " ,i)
#4.Write a function to test if array contains a specific value.
arr= list(map(int,input().split()))
n = int(input("Enter the element:"))
def check(arr,n):

    for i in range(len(arr)):
        if arr[i] == n:
            return "It is in Array"
    return "It is not in Array"
test = check(arr,n)
print(test)
#5. Write a function to remove a specific element from an array
arr= list(map(int,input().split()))
n = int(input("Enter the element:"))
def delete(arr,n):
    new_arr=[]
    for i in arr:
        if i != n:
            new_arr.append(i)
    return new_arr
test = delete(arr,n)
print(test)
#6. Write a function to copy an array to another array.
arr= list(map(int,input().split()))
def copy(arr):
    new_arr=arr[:]
    return new_arr
test = copy(arr)
print("New Array:",test)
#7. Write a function to insert an element at a specific position in the array
arr= list(map(int,input("Enter array:").split()))
n= int(input("Enter the element:"))
a= int(input("Enter the position:"))
def insert(arr,n,a):
    arr.append(0)
    for i in range(len(arr)-1,a,-1):
        arr[i] = arr[i-1]
    arr[a] = n
    return arr
test = insert(arr,n,a)
print("New Array:",test)
#8. Write a function to find the minimum and maximum value of an array
arr= list(map(int,input("Enter array:").split()))
def minimaxi(arr):
    mini = arr[0]
    maxi = arr[0]
    for i in range(0,len(arr)):
        if arr[i]< mini:
            mini = arr[i]
        if i > maxi:
            maxi = arr[i]
    return mini,maxi
mini,maxi = minimaxi(arr)
print("Mininmum:",mini,"Maximum:",maxi)
#9. Write a function to reverse an array of integer values.
arr= list(map(int,input("Enter array:").split()))
def reverse(arr):
    return arr[::-1]
rev = reverse(arr)
print("Reversed Array:",rev)
#10. Write a function to find the duplicate values of an array 
arr = list(map(int, input().split()))
new_arr = []
seen = set()
def duplicate():
    for i in arr:
        if i in seen and i not in new_arr:  
            new_arr.append(i) 
        else:
            seen.add(i) 
    return new_arr

duplicate_values = duplicate()
print(duplicate_values)
#11.Write a program to find the common values between two arrays
arr1= list(map(int,input("Enter array1 elements:").split()))
arr2= list(map(int,input("Enter array2 elements:").split()))
def common(arr1,arr2):
    com=[]
    for i in arr1:
        if i in arr2:
            com.append(i)
    return com
c=common(arr1,arr2)
print("Common Elements of 2 Arrays:",c)
#12. Write a method to remove duplicate elements from an array
arr= list(map(int,input("Enter array elements:").split()))
def duplicate(arr):
    dup = []
    for i in arr:
        if i not in dup:
            dup.append(i)
    return dup
unique = duplicate(arr)
print("Unique Elements:",unique)
#13.  Write a method to find the second largest number in an array
arr= list(map(int,input("Enter array elements:").split()))
def sec_lar(arr):
    first, sec = float('-inf'),float('-inf')
    if len(arr) < 2:
        return "There is no second largest"
    for i in range(len(arr)):
        if arr[i]> first:
            sec, first = first, arr[i]
        elif first > arr[i]> sec:
            sec = arr[i]
    return sec
sl = sec_lar(arr)
print("Second Largest Elements:",sl)
#14. Write a method to find the second largest number in an array 
arr= list(map(int,input("Enter array elements:").split()))
def sec_lar(arr):
    first, sec = float('-inf'),float('-inf')
    if len(arr) < 2:
        return "There is no second largest"
    for i in range(len(arr)):
        if arr[i]> first:
            sec, first = first, arr[i]
        elif first > arr[i]> sec:
            sec = arr[i]
    return sec
sl = sec_lar(arr)
print("Second Largest Elements:",sl)
#15. Write a method to find number of even number and odd numbers in an array
arr= list(map(int,input("Enter array elements:").split()))
def even_odd(arr):
    even =[]
    odd= []
    for i in arr:
        if i % 2==0:
            even.append(i)
        else:
            odd.append(i)
    return "Even:",len(even),"Odd:",len(odd)
print(even_odd(arr))
#16.Write a function to get the difference of largest and smallest value.
arr= list(map(int,input("Enter array elements:").split()))
def diff(arr):
    max,min= arr[0],arr[0]
    for i in arr:
        if i <min:
            min= i
        if i> max:
            max = i
    return max - min
print(diff(arr))
#17. Write a method to verify if the array contains two specified elements(12,23).
arr = list(map(int, input("Enter array elements: ").split()))

def check(arr):
    found = [i for i in arr if i in (12, 23)]  
    
    if found:
        print("It contains:", *found)  
    else:
        print("Not present")

check(arr)
#18. Write a program to remove the duplicate elements and return the new array 
arr= list(map(int,input("Enter array elements:").split()))
def duplicate(arr):
    dup = []
    for i in arr:
        if i not in dup:
            dup.append(i)
    return dup
unique = duplicate(arr)
print("Unique Elements:",unique)
