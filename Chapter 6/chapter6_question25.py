def main():
    x = 7
    y = 5
    z = 6
    compute(x, y, z)
    print(x+y+z)
    
def compute(x, y, z): #7,5,6
       y = 1
       x = y + z # x = 1 + 6 --> x = 7
       z = x * y # 6 = 7 * 1 --> z = 7
       print(x+y+z, end = '\n') # 15
       return()
    
# The entry point for program execution
if __name__ == "__main__":
 main()


# Pass by Value question where compute() gets it's own copy of (x,y,z)
