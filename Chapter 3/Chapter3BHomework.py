# Question 15
def q15():
    m = 12
    while m >= 0:
        m -= 3
        if m % 2 == 0:
            print(m, end = ' ')
    print(m)

# Question 17
def q17():
    e = 20
    while e > 0:
        print(e, end = ' ')
        e -= 5
    print(e)

# Question 19
'''
x = 1
while x < 10:
    print(x)
'''

# Question 20:
def q20():
    x = 1
    while x < 10:
        print(x)
        x += 2

# Question 21:
def q21():
    a = 10
    while a > 0:
        print(a)
        a -= 1
        break

# Question 22:
def q22():
    x = 5; y = 20;
    print(not(y<15))
    print((x == 5) or (x !=5))
    print((x > 0) and (y != 20))
    print((x > 0) or (y != 20))
    print((x // y > 0) and (y > x))


def q25():
    x = 100
    y = 25
    if x > 75 or y < 30 and x % y != 0:
        print(1)
    else:
        print(0)
q25()

def q27():
    import random
    h = random.randint(1,5)
    print(h)
q27()