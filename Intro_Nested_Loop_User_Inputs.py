# Shawn Kahele
# 10/22/2026
# Use nested loops to validate user inputs

# Create an empty list
valid_grades = []

# Get number of scores from user as int
num_of_scores = int(input("How many grades will you enter? "))

# Make a for loop that runs num_of_scores times
for scores in range(1, num_of_scores + 1):
    input_score = float(input(f"Enter score #{scores}: "))
    
    # while loop that traps the user while input_score is invalid
    while input_score < 0 or input_score > 100:
        print("Invalid grade entered!")
        print("Score should be between 0 and 100")
        # Ask user for a new value for input_score
        input_score = float(input(f"Enter score #{scores} again: "))
    
    # Add input_score to the valid_grades list
    valid_grades.append(input_score)

# All loops are broken
print(valid_grades)