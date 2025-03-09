#1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
dictionary = {
    "Student1_ID" : "22048",
    "Student2_ID" : "22049",
    "Student1_Name": "Bhanu",
    "Student2_Name": "Sri",
    "Student3_ID": "22050",
    "Student3_Name":"Bhagath"
}
print(dictionary)
#1.1. Adding the values in dictionary.
dictionary = {
    "Student1_ID" : 22048,
    "Student2_ID" : 22049,
    "Student1_Name": "Bhanu",
    "Student2_Name": "Sri",
    "Student3_ID": 22050,
    "Student3_Name":"Bhagath" 
}
dictionary["Student4_ID"] = 22051 # adding student4
print(dictionary)
#1.2. Updating the values in dictionary
dictionary = {
    "Student1_ID" : 22048,
    "Student2_ID" : 22049,
    "Student1_Name": "Bhanu",
    "Student2_Name": "Sri",
    "Student3_ID": 22050,
    "Student3_Name":"Bhagath" 
}
dictionary.update({"Student2_Name": "Sudha"}) # updating student name
print(dictionary)
#1.3. Accessing the value in dictionary 
dictionary = {
    "Student1_ID" : 22048,
    "Student2_ID" : 22049,
    "Student1_Name": "Bhanu",
    "Student2_Name": "Sri",
    "Student3_ID": 22050,
    "Student3_Name":"Bhagath" 
}
print(dictionary["Student3_ID"]) 
print(dictionary.get("Student3_ID")) # by using get method
#1.4. Create a nested loop dictionary 
dictionary = {
    "Student1":{
        "Name": "Bhanu",
        "ID" : "22050",
        "Subjects":{
            "CS": 90,
            "DS": 70,
        }
    },
    "Student2":{
        "Name":" Bhagath",
        "ID" : "22051",
        "Subjects":{
             "CS": 95,
            "DS": 75,
        }
    }
}

#1.5. Access the values of nested loop dictionary
dictionary = {
    "Student1":{
        "Name": "Bhanu",
        "ID" : "22050",
        "Subjects":{
            "CS": 90,
            "DS": 70,
        }
    },
    "Student2":{
        "Name":" Bhagath",
        "ID" : "22051",
        "Subjects":{
             "CS": 95,
            "DS": 75,
        }
    }
}
#Accessing the values of nested loop dictionary.
for student, details in dictionary.items():
    print(f"\n{student} - Name: {details['Name']}, ID: {details['ID']}")
    print(" Subjects:", ", ".join(f"{sub}: {marks}" for sub, marks in details["Subjects"].items()))
  
#1.6. Print the keys present in a particular dictionary 
dictionary = {
    "Student1_ID" : "22048",
    "Student2_ID" : "22049",
    "Student1_Name": "Bhanu",
    "Student2_Name": "Sri",
    "Student3_ID": "22050",
    "Student3_Name":"Bhagath"
}
for students,details in dictionary.items():
    print(f'{students}')

#1.7. Delete a value from a dictionary
dictionary = {
    "Student1_ID" : "22048",
    "Student2_ID" : "22049",
    "Student1_Name": "Bhanu",
    "Student2_Name": "Sri",
    "Student3_ID": "22050",
    "Student3_Name":"Bhagath"
}
dictionary.pop("Student2_Name")
print(dictionary)
