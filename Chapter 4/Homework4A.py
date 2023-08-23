def stringSplit():
    sentence = input("Enter a sentence, please. ")
    listOfWords = sentence.split()
    g = 0
    for words in listOfWords:
        if len(words) > g:
            g = len(words)
    print("g is ", g)

def stringFind():
    phrase = "The rain in Spain."
    a = phrase.find('in')
    print(a)

"""
message = "catapult"
print(message[5])

f = "Autumn Leaves"
for index in range(len(f)):
    print(index, f[index])
"""
def Question8():
    f = "Autumn Leaves"
    j = f[:5]
    print(j)

def combinedStringFunctions():
    j = "Red,Blue,Green,Orange,Purple"
    jList = j.split(',')[-2]
    print(jList)
    # Output -> Orange

"""
name = "Florence Nightingale"
print(name[10:])
"""

"""
word = "Green Tree"
i = len(word)
print(word[i])
"""

def Question14():
    x = "Computer Programming"
    y = x[-4:]
    print(y)
    # output will be 'ming'. The last four characters of the string

def Question15():
    s = "TeSt12#"
    lowerCase = s.lower()
    upperCase = s.upper()
    print(lowerCase, upperCase)

def Question16():
    group = "Ellen Sara Alice Peter Fred George Brad"
    groupList = group.split("E");
    print(groupList)

def Question17():
    roster = "Horace Bud-Dale Flora-Fauna Sabrina-Michah Greg"
    rList = roster.split('-')
    print(rList)

def Question18():
    place = "The Lost Valley"
    part = "valley"
    if part in place:
        x = True
    else:
        x = False
    print(x)
    """
    Here we see that part is case sensitive. 
    Therefore x will results in false.
     """
