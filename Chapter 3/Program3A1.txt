# Title:    Program3A1
# Author:   Nicholas Arvo
# Purpose:  This program will take user input on hourly wage and 
#           total hours worked to calculate and present back an employee's weekly pay.

# Prompt for hours worked and pay rate
totalHours = float(input("How many hours did the employee work this week: "))
payRate = float(input("What is the employee's hourly pay rate? "))

# Calculate how many, if any, hours the employee worked overtime. Print appropriate pay.
regularHours = 40

if totalHours > regularHours:
    overtimeHours = totalHours - regularHours
    regPay = 40 * payRate
    overtimePay = overtimeHours * (payRate * 1.5)
    totalPay = regPay + overtimePay
    print(str(regularHours) + " regular and " + str(overtimeHours) + " overtime at " + str(payRate) + " = " + str(totalPay))
else:
    totalPay = totalHours * payRate
    print(str(regularHours) + " regular at " + str(payRate) + " = " + str(totalPay))
