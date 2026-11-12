# Shawn Kahele
# 10/15/2026
# Use a for loop and a while loop to draw shapes

import turtle

# Set up the window and drawing object (turtle)
window = turtle.Screen()
lolo = turtle.Turtle()

lolo.pensize(3)
lolo.pencolor("blue") 

# For loop to draw a square
for side in range(4):
    lolo.forward(200)
    lolo.right(90)

# while loop that draws a triangle
num = 1
while num <= 3:
    # draw a side
    lolo.forward(200)
    lolo.left(120)
    # increment num
    num = num + 1

# Keep window open
window.mainloop()