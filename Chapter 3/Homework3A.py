# Question 1
x = 4
y = 6
print((x-y)**2 > y)
#(4-6)^2 > 6
#-2^2 > 6
# 4 > 6 -> False

# Quetion 2
var1 = 25
print("%d"%var1)

# Question 8
total = 17.15
print("The total is %.5f"%total)

# Question 9
for count in range(10, 3, -1):
    print(count)

# Question 14
i = 3
if i < 10:
    print('hello')
print('goodbye')

# Question 16
e = 3; f =14;
if e != 10:
    print('hello')
if f < 10:
    print('howdy')
print('goodbye')

# Question 17
f = 5; e = 10;
if e - f > 5:
    print(f)
elif e - f < 5:
    print(e)
else:
    print(e*2)

# Question 18
a = 15; b = 17;
if a == 16:
    a *= 2
elif b > 17:
    a /= 3
print(a)

# Question 19 with input 4, 7, 12, 9
'''sum = 0;
for j in range(4):
    num = int(input("Enter a number: "))
    sum += num
print(sum)'''

# Question 20
a = 0
for b in range(5):
    a += 1
print("the value of a is: ", a)

# Question 21
for x in range(6):
    print(x, end = ' ')

# Question 22    
print('\n')
for x in range(1,7):
    print(x, end = ' ')

# Question 23
print('\n')
z = 0;
for x in range(3,10):
    z = z + x;
print("The value of z is:", z)

# Question 24
for c in range(5,25):
    print('X', end = ' ')
    print('The value of c is now: ', c)
print('\n')

# Question 25
j = 0;
for x in range (1,6,2):
    j += x
print("The value of j is: ", j)

# Question 26
for z in range(8,0,-2):
    print("Alert", end = ' ')

# Question 28
j = 83.950112
print('\n')
print("%.2f"%j)
print('\n')

# Question 29 Left and right aligned text
h = 10000
print("%-8d"%h)
print('%8d'%h)