# Shawn Kahele
# 9/29/26
# P3HW1 Grade and Grade Average
# Creating min, max, sum, and average for user's grade(s) stored in a list

import math

print()

# Engaging user for information
print("To find your current grade status, please enter the following information.")
print()

#Collecting grades from user
one = float(input("Enter your grade for Module 1: "))
two = float(input("Enter your grade for Module 2: "))
three = float(input("Enter your grade for Module 3: "))
four = float(input("Enter your grade for Module 4: "))
five = float(input("Enter your grade for Module 5: "))
six = float(input("Enter your grade for Module 6: "))

# Creating list from user's input, assigning to variable
grades = [one, two, three, four, five, six]

# Utilizing math library to calculate min, max, sum, avg
low = min(grades)
high = max(grades)
total = sum(grades)
length = len(grades)
avg = total / length
print()

# Displaying results to user 
print("---------------Results---------------")
print()
print(f"{'Lowest Grade:':<20}{low:.2f}")
print(f"{'Highest Grade:':<20}{high:.2f}")
print(f"{'Sum of Grade:':<20}{total:.2f}")
print(f"{'Average':<20}{avg:.2f}")

print("-------------------------------------")

# Round average to the nearest integer
avg = round(avg)


# Branching to determine letter grade based on the average
if avg >= 90:
    grade_report = "A"
elif avg >= 80:
    grade_report = "B"
elif avg >= 70:
    grade_report = "C"
elif avg >= 60:
    grade_report = "D"
else:
    grade_report = "F"

print()
print(f"Your average is {avg}, so your letter grade is {grade_report}")
print()
print("Thank you for using the Grade Average Calculator!")
print()