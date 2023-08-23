def main():
    nbrlist = [10, 20, 30]
    x = 3.5
    y = 2.0
    j, k, m, n = processNums(x, y)
    print("j:", j)
    print("k:", k)
    print("m:", m)
    print("n:", n)
    
def processNums(a, b): # Arguements = (3.5, 2.0)
       c = a + b # 3.5 + 2.0 --> 5.5
       d = a - b # 3.5 - 2.0 --> 1.5
       e = a * b # 3.5 * 2.0 --> 7.0
       f = a / b # 3.5 / 2.0 --> 1.75
       return c, d, e, f
    
# The entry point for program execution
if __name__ == "__main__":
 main()
