from math import pi

TEST = "GLOBAL STRING"

def calcArea(radius):
    area = pi * radius ** 2
    return area

def calcVolume(radius):
    volume = pi * radius **3
    global TEST
    TEST = 'modified'
    return volume

print(TEST)
rad = float(input("Please enter a radius: "))
a = calcArea(rad)
v = calcVolume(rad)
print("Radius %0.2f, Area: %0.2f, Volume: %0.2f" %(rad,a,v))
print(TEST)