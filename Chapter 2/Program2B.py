# Title:    Program2B
# Author:   Nicholas Arvo
# Purpose:  This program calculates the average speed when given distance and time.

distance = float(input('Please enter the distance traveled in miles: '))
time = float(input('Please enter the total travel time in hours: '))
speed = distance/time

print('Distance covered: ' + str(round(distance,3)) + ' miles')
print('Travel Time: ' + str(round(time,3)) + ' hours')
print('Average Traveling Speed: ' + str(round(speed,3)) + ' miles per hour')


