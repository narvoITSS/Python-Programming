"""
ComputeCylinder
Nicholas Arvo
This program will compute the volume and surface area
of a cylinder.
"""
from math import pi

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

surfaceArea = (2 * pi * radius ** 2) + (pi * 2 * radius * height)
volume = (pi * radius ** 2) * height

print("The surface area is: ", round(surfaceArea,3))
print("The volume is: ", round(volume,3))

