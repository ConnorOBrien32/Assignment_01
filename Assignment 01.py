# Team Members: Connor O'Brien
# Course: CS151, Prof. Mehri
# Date: September 27, 2021
# Programming Assignment: 1
# Program Inputs: lenght, width, height (in feet)

# Program Outputs: Computes the total area of the four walls and ceiling,
# and determines the amount of primer and paint (in gallons) necessary to cover them

# Assume one gallon of primer will coat 200 square feet and
# one gallon of paint will cover 350 square feet

# Output purpose
print("This program computes the gallons needed for primer and paint.")

# Ask user for the length in feet
length = input("Please enter the length of a room in feet: ")
length = float(length)

# Ask the user for the width in feet
width = input("Please enter the width of a room in feet: ")
width = float(width)

# Ask the user for the height in feet
height = input("Please enter the height of the room in feet: ")
height = float(height)

area_of_wall = 2*width*height+2*width*height

area_of_ceiling = length*width

primer_needed = area_of_ceiling/200
primer_needed2 = area_of_wall/200

paint_needed = area_of_ceiling/350
paint_needed2 = area_of_wall/350

print("The amount of primer to coat the ceiling", primer_needed, "and to coat the walls", primer_needed2,)

print("The amount of paint needed to coat the ceiling", paint_needed, "and for the walls", paint_needed2,)