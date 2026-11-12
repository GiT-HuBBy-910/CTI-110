# Shawn Kahele
# 9/15/2026
# Calculate components of a circle using pi from math library

import math

# Print the value of Pi
print(math.pi)
print()

# Get radius from user
radius = float(input("Enter the radius: "))

print()

# Calculate the Diameter
diameter = 2 * radius

# Display radius
print(f"The diameter of a circle is {diameter:.1f}")

# Calculate the Circumference
circumference = 2 * math.pi * radius

# Display circumference using the f-string
print(f"The circumference of the circle is {circumference:.2f}")

# Calculate the area
area = math.pi * math.pow(radius, 2)

# Display the area with an f-string
print(f"The area of the circle is {area:.3f}")