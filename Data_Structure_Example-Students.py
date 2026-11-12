
# Learn to use Dictionaries
# Each entry consists of a key:value pair

# Create a dictionary where the keys are student IDs and values are names
students = {"001":"Kevin", "002":"Suzie", "003":"Kate"}

# Check if you did it right
print(students)
print()

# Give the key, have Python return the value
print(students["003"])
print(students["002"])
print(students["001"])
print()

# Get the student id from the user
student_id = input("Enter a student ID: ")

# Using the student_id from the user, have Python return value
print(students[student_id])
print()

# Add a key:value pair into an existing dictionary
students["004"] = "Dion"
print(students)
print()

# Delete a key:value pair from the dictionary
del students["001"]
print(students)
print()
print()
print("Yay, Kevin graduated!")