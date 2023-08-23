# Title:    Lab6A2
# Author:   Nicholas Arvo
# Purpose:  This program will read an unknown number of intergers marked by line breaks
#           from a text file and then add up the digits in each number.


def addDigits(number):
    number = list(number)
    sum = 0
    for index in range(len(number)):
        number[index] = int(number[index])
        sum += number[index] # running total of digits
    return(sum)

def main():
    file = open("Lab6A2.txt", 'r')
    for line in file:
        line = line.strip()
        print("The sum of all the digits in '" + line + "' is:", addDigits(line))

if __name__ == "__main__":
    main()
