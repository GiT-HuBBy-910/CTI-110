# Shawn Kahele
# 9/10/2026
# Travel Expenses
# This program calculates and dispalys travel expenses
print()
print()

# Instruction for user to engage for inputs
print("To calculate your travel expenses, please enter your information below")

print()
# Taking in int value for initial budget, assigning it to variable, budget
budget = int(input("Enter Budget: "))

print()
# Taking in string value for location, assigning it to variable, location
location = str(input("Enter your travel destination: "))

print()
# Taking in int value for gas budget, assigning it to variable, gas
gas = int(input("How much do you think you will spend on gas?: "))

print()
# Taking in int value for accomodation, assigning it to variable, hotel
hotel = int(input("Approximately how much will you need for accomodation/hotel?: "))

print()
# Taking in int value for food budget, assigning it to variable, food
food = int(input("Last, how much do you need for food?: "))

print()
print()
 
# Assigning value of variable to string label
print("-------------Travel Expenses---------------")

print("Location: ", location)
print("Intial Budget: ", budget)

print()

print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)

# Calculating remaining balance
print()

total = budget - gas - hotel - food

print("Remaining Balance: ", total)