def main():
       x = 3
       y = 2
       z = calcData(x, y)
       w = doStuff(x, y)
       print(z + w)

def calcData(a, b):
       c = a ** b
       return c # 3^2 = 9

def doStuff(j, k):
       m = 25 % j + k;
       #print(doStuff.__name__)
       return m; # 25%3+2 --> 1 + 2 = 3

# The entry point for program execution
if __name__ == "__main__":
 main()
