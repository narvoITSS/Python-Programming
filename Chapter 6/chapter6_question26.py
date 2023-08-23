def main():
    nbrlist = [2, 4, 6, 8, 10]
    processList(nbrlist)
    print(nbrlist[2])
    
def processList(list):
       for i in range(len(list)):
           list[i] = list[i] / 2
    
# The entry point for program execution
if __name__ == "__main__":
     main()
