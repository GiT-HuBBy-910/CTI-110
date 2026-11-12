# Notes - Aligning, integer, float, list, dynamic width, string padding, split mode

# Create float variables for the adoption costs
dog_fee = 50.55
penguin_fee = 8000.00
parrot_fee = 2000.99
cat_fee = 18

# Create integer variables (NOT in HW)
dog_quantity = 7
penguin_quantity = 2
parrot_quantity = 12
cat_quantity = 28

# Display using string formatting
print(f"{'ANIMAL TYPE':<16}{'ADOPTION FEE':<17}{'QUANTITY':<16}")
print('-' * 50)

print(f"{'Dog':<16}${dog_fee:<17,.2f}{dog_quantity:<16}")
print(f"{'Penguin':<16}${penguin_fee:<17,.2f}{penguin_quantity:<16}")
print(f"{'Parrot':<16}${parrot_fee:<17,.2f}{parrot_quantity:<16}")
print(f"{'Cat':<16}${cat_fee:<17,.2f}{cat_quantity:<16}")

print()
print()

# Self Notes: Displaying List Data in a Structured Table

d = [("Alice", 25, "USA"), ("Char", 22, "Chicago")]

print(f"{'Name':<10}{'Age':<5}{'City':<10}")

for name, age, city in d:
    print(f"{name:<10}{age:<5}{city:<10}")

print()
print()

# Self Notes: Handling dynamic width

a = ["Apple", "Banana", "Cherry"]
max_width = max(len(word) for word in a) + 2
for word in a:
    print(f"{word:<{max_width}} - Fruit")

print()
print()

# Self Notes: String padding for enhanced formatting
s = "Python"

print(f"{s:-^20}")  
print(f"{s:*<15}")  
print(f"{s:=>15}")

print()
print()

# Using split mode to allow user to input 2 numbers
# User must use space between number, or it will cause an error

x, y = input("Enter two numbers: ").split()
print(x , y)