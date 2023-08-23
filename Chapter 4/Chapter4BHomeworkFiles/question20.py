infile = open("question18.txt", 'r')
line = infile.read()
list = line.split()
word = list[-1]
num = int(word)
print(num)
