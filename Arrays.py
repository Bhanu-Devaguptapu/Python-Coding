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
