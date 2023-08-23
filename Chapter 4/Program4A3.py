# Title:    Program4A3
# Author:   Nicholas Arvo
# Purpose:  This program asks the user to enter a password that must
#           meet password complexity requirements. The user will be
#           told which requirements their password fails to meet if any.

password = input("Please enter a password: ")

# 1) password must be >= 8 characters
if len(password) < 8:
    print("ERROR! Your password must be eight or more characters in length.")

# 2) password must have at least one number
numberCount = 0
for index in range(len(password)):
    if password[index].isdecimal():
        numberCount += 1
if numberCount < 1:
    print("ERROR! Your password must contain at least one number.")

# 3) password must have a special character (!, &, *, %, $)
specialCharcters = "!,&,*,%,$"
specialCharacters = specialCharcters.split(',')

specialFlag = False # used to mark if special char is found

for char in specialCharcters:
    if char in password:
        specialFlag = True
if specialFlag == False:
    print("ERROR! Your password does not contain at least one special character (!, &, *, %, $).")
