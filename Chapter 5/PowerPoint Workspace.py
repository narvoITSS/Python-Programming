# to change the value of list elements at index values
def replacingElementsInList():
    numbers = [2,3,4,5]
    for index in range(len(numbers)):
        numbers[index] = numbers[index]**2
    print(numbers)

def replacingElementsInList2():
    sentence = "This example has five words."
    words = sentence.split()
    for index in range(len(words)):
        words[index] = words[index].upper()
    print(words)

