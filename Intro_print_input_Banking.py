# Shawn Kahele
# 9/8/2026
# Simulate banking

# Get the name of the user

customer_name = input("Enter your name: ") 

#Display welcome message

print(customer_name, "Welcome to Simulation Bank.")

# Get initial balance from user

balance = 1000

print("Your current balance is:",balance)

# Get amount to withdraw
withdraw_amount =  float(input("Enter the amount to withdraw: "))

# Do calculations
new_balance = balance - withdraw_amount

# Display balance

print("Your current balance is:", new_balance)