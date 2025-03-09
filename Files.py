#1. Reading a text file
def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:\n", content)
    except FileNotFoundError:
        print("File not found!")
read_text_file("example.txt")
#2. # Writing to a text file
def write_to_file(filename):
    with open(filename, 'w') as file:
        text = input("Enter text to write to file: ")
        file.write(text)
        print("Text written successfully!")
write_to_file("output.txt")
#3.  Reading file using file stream (buffered read)
def read_file_stream(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')  # Reads line by line
    except FileNotFoundError:
        print("File not found!")
read_file_stream("example.txt")
#4. Write a program to read a file stream supports random access 
def random_access_read(filename, position):
    try:
        with open(filename, 'r') as file:
            file.seek(position)  # Move to the desired position
            print("Reading from position:", position)
            print(file.read())  # Read from that position onwards
    except FileNotFoundError:
        print("File not found!")

# Example Usage
random_access_read("example.txt", 10)
#5.Write a program to read a file a just to a particular index using seek() 
def read_at_index(filename, index):
    try:
        with open(filename, 'r') as file:
            file.seek(index)  # Move to the index
            print("Character at index", index, ":", file.read(1))  # Read one character
    except FileNotFoundError:
        print("File not found!")
read_at_index("example.txt", 5)
#6 Write a program to check whether a file is having read access and write access permissions
import os

# Checking file permissions
def check_file_permissions(filename):
    if os.path.exists(filename):
        print(f"Read Permission: {'Yes' if os.access(filename, os.R_OK) else 'No'}")
        print(f"Write Permission: {'Yes' if os.access(filename, os.W_OK) else 'No'}")
    else:
        print("File does not exist!")
check_file_permissions("example.txt")
