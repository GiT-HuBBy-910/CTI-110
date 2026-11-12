# Shawn Kahele
# 9/10/2026
# Inputs and Outputs, and mathematical calculations

# Get base value from user and convert to int
base_value = int(input ("Enter a base value: "))

# Get exponent from user and convert to int
exponent = int(input ("Enter an exponent: "))

# Calculate
answer = base_value ** exponent

# Display answer
print(base_value, "raised to the power of", exponent,"is", answer)

print()
print()

print("-----------Addition and Subtraction------------")
print()
print()

# Get three integers from user
num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter number to add: "))
num3 = int(input("Enter number to subtract: "))

print()

# Display the results

print(num1, "+",num2, "-", num3, "=", num1 + num2 - num3)

answer2 = num1 + num2 - num3

print(num1, "+", num2, "-", num3, "=", answer2)