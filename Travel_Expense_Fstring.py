# Shawn Kahele
# 9/16/2026
# Cleaner Travel Expense Display Using Float Input Output
# This program calculates and dispalys travel expenses to the user

print()
print()

# Instruction to user for inputs
print("To calculate your travel expenses, please enter your information below")
print("----------------------------------------------------------------------")
print()

# Assigning user values to variables
budget = float(input("Enter Budget: "))

print()
location = input("Enter your destination: ")

print()
gas = float(input("How much do you think you will spend on gas?: "))

print()
hotel = float(input("Approximately how much will you need for accomodation/hotel?: "))

print()
food = float(input("Last, how much do you need for food?: "))

print()
print()
 
# Displaying user's input with labels
print("--------------------Travel Expenses---------------------")
print()

# Aligning information into columns
print(f"{'Location: ':<28}\U0001f600 {location}")
print("--------------------------------------------------------")
print(f"{'Intial Budget:':<30}${budget:.2f}")
print(f"{'Fuel:':<30}${gas:>.2f}")
print(f"{'Accomodation:':<30}${hotel:.2f}")
print(f"{'Food:':<30}${food:.2f}")
print()

# Calculating remaining balance
total = budget - gas - hotel - food
print("--------------------------------------------------------")
print(f"{'Remaining Balance:':<30}${total:.2f}")
print()