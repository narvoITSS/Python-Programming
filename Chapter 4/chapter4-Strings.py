def lengthFunction():
    test_string = 'Hello world!'
    print(len(test_string))

# Subscript Operators
def subscriptOperator1():
    name = 'alan turning'
    print(name[0]) # Examine the first char 'A'
    print(name[len(name)-1]) # print the last character
    print(name[-1]) # shorthand for print the last character
    print(name[-2]) 

# Subscript Continued
def subscriptOperator2():
    data = 'Hi there!'
    print(len(data))
    for index in range(len(data)):
        print(index, data[index])

# Slicing strings with subscript operator
def slicingForSubstrings():
    name = 'myfile.txt'
    print(name[3:])
    print(name[1:4]) # notice like a for loop does not include the char at the end value
    print(name[-3:])
#slicingForSubstrings()

def encryption():
    plainText = input("Please enter a one-word, lowercase message: ")
    cipherDistance = int(input("Enter a distance value for the cipher: "))
    code = ' '
    for ch in plainText:
        ordValue = ord(ch)
        cipherValue = ordValue + cipherDistance
        
        if cipherValue > ord('z'):
            cipherValue = ord('a') + cipherDistance - (ord('z') - ordValue + 1)
        code += chr(cipherValue)
    print(code)
#encryption()

def binaryToDecimal():
    bitString = input("Enter a string of bits: ")
    decimal = 0
    exponent = len(bitString)-1

    for digit in bitString:
        decimal = decimal + int(digit) * 2 ** exponent
        exponent -= 1

    print("the integer value is: ", decimal)
binaryToDecimal()

def decimalToBinary():
    decimal = int(input("Enter a decimal integer: "))
    if decimal == 0:
        print(0)
    else:
        print("Quotient Remainder Binary")
    bitString = " "
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitString = str(remainder) + bitString
        print("%5d%8d%12s" % (decimal, remainder, bitString))
    print("The binary representation is: ", bitString)
decimalToBinary()

def writingExample1():
    f = open("myFile.txt", 'w')
    f.write("First line\nSecond Line\n")
    f.close()
    #f = open("myFile.txt", 'w')
    """ you can see that if you open the text file after closingS the prior contents are erased."""

def writingExample2():
    import random
    f = open("random integers.txt", 'w')
    for count in range(500):
        numbers = random.randint(1, 500)
        f.write(str(numbers) + '\n')
    f.close()
#writingExample2()

def readingTextFromFile():
    f = open("myFile.txt", 'r')
    text = f.read()
    print(text)
    #g = open("random integers.txt", 'r')
    #text = g.read()
    #print(text)
#readingTextFromFile()

def removingEmptyString():
    # the read method will append an emptry string
    # at the end of a file

    f = open("myFile.txt", 'r')
    line = 'debug'
    while line != "":
        line = f.readline()
        if line != "":
            line = line.strip()
            print(line)
#removingEmptyString()

def numbersFromFile1():
    ''' 
        remember python will read into and out from files as strings
        thus data must be typecasted if you want an integer or flot
    '''
    f = open("random integers.txt", 'r')
    theSum = 0
    for line in f:
        line = line.strip()
        number = int(line)
        theSum += number
    print("The sum is: ", theSum)


def numbersFromFile2():
    f = open("random integers.txt", 'r')
    theSum = 0
    for line in f:
        # here we use split to allow integers seperated by spaces or newlines to be added
        wordlist = line.split()     
        for words in wordlist:
            number = int(words)
            theSum += number
        
    print("The sum is", theSum) 
#numbersFromFile1()

#f = open("random integers.txt",'r')
##line = f.readline().strip()
#print(line)
