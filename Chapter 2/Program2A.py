# Title:    Program2A
# Author:   Nicholas Arvo
# Purpose:  This program ask the user for input on two variables: mass and velocity, then uses those
#           variables to calculate the corresponding velocity.

mass =      float(input("Please enter the object\'s mass: "))
velocity =  float(input("Please enter the object\'s velocity: "))
momentum = mass*velocity

print("The object\'s momentum is", momentum)

