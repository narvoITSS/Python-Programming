# Pass by Value

num = 5
numList = [5]

def double(n):
    n *= 2
    return

def doubleList(nList):
    nList[0] *= 2
    return

# Pass By value
print("Before function call: ", num)
double(num)
print("After function call: ", num)
print()

#Pass By Reference
print("Before function call: ", numList)
doubleList(numList)
print("After function call: ", numList)
