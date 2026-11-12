
# Shawn Kahele
# 9/17/2026
# P2LAB2
# Using dictionary to determine amount of fuel needed from user inputs

# Creating a dictionary - cars are the keys and mpgs are the value
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Select only the keys
keys = cars.keys()
 
# Display the keys
print(keys)
print()

# Get a car choice from the user
car_choice = input("Enter a car to see it's mpg: ")
print()

# Using car_choice to pull the associated mpg from dictionary
mpg = cars[car_choice]

# Display car choice and mgp back to user
print(f"The {car_choice} gets {mpg} mpg.")

# Get miles to drive from user as a float
miles = float(input(f"How many miles will you drive the {car_choice}? ")) 

# Calculate gallons of gas needed
gallons = miles/mpg

# Display results back to user, with vehicle choice and miles driven
print(f"{gallons:.2f} gallons of gas are needed to drive the {car_choice} {miles} miles")