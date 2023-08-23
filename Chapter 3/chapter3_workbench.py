def definiteForLoop():
    sum = 0
    for a in range(6):
        sum = sum + a
        print("The value of a: ", a)
        print("Sum this iteration is equal: ", sum)
    print("Final sum is: ", sum)
     # Output should be 15

     # You can see that the loop will iterate to the Range - 1.
     # Thus a goes from 0, 1, 2, 3, 5

def explicitLowerBound(): # Here 1 is the explicit lower bound
    product = 1
    for count in range(1,5):
        product = product * count
    print(product)
    # Output will be 24

def examiningRange(): # off-by-one errors
    print(list(range(4))) # here we a list of [0,1,2,3]

def iteratingThroughString(): # Strings are a sequence of characters that be iterated through
    for character in "Hi there!":
        print(character, end = ' ') # the 'end' arguement effects the print statement
    # Output should be H i  t h e r e !

# Range has a third argument that you can provide for each "Step" of the iteration
def rangeStepExample():
    print(list(range(1,99,2))) # print every other number or every odd number

def formatTest():
    for exponent in range(7,11):
        print("%-3d%12d" % (exponent, 10 ** exponent))

def formattingFloatDecimals():
    salary = 100.00
    print("Your salary is $", salary)
    print("Your salary is $%0.2f" % salary)
    #%<field width>.<precision>f

def selectionStatements():
    x = int(input("Enter a number: "))
    if x < 0:
        x = -x  # this statement only happens if x is less than 0
    print(x)

def twoWaySelectionStatements(): # often used to check input for errors
    import math
    area = float(input("Enter the area: "))
    if area > 0:
        radius = math.sqrt(area / math.pi)
        print("The radius is", radius)
    else:
        print("Error: the area must be a positive number!")

def multiWaySelectionStatements():
    number = int(input("Enter the number grade: "))
    if number > 89:
        letter = 'a'
    elif number > 79:
        letter = 'b'
    elif number > 69:
        letter = 'c'
    else:
        letter = 'f'
    print("The letter grade is", letter)

def whileVSFor():
    theSum = 0
    for count in range(1,100001):
        theSum += count
    print(theSum)

    theSum = 0
    count = 1
    while count <= 100000:
        theSum += count
        count += 1
    print(theSum)

def breakStatement():
    sum = 0.0
    count = 0
    while count <= 4:
        value = float(input("Enter a grade: "))
        if value < 0:
            print("Error - grades cannot be negative.")
            break   # should exit the while loop. notice the scope
        sum += value
        count += 1

    print("the sum is: ", sum)
    average = sum/count
    print("Average is: ", average)

def randomNumbers():
    from random import randint
    for roll in range(10):
        print(randint(1,6), end = ' ')
randomNumbers()
