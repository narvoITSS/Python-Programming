# Title:    Program2C
# Author:   Nicholas Arvo
# Purpose:  Take input from the user to determine radius and then calculate
#           the diameter, circumference, and area.

from math import pi

radius = float(input("Enter the value of the radius: "))
diameter = radius * 2
circumference = pi * diameter
area = pi * radius ** 2

print("Diameter:", round(diameter,2))
print("Circumference:", round(circumference,2))
print("Area:", round(area,2))
