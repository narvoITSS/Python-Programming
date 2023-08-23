infile = open("question18.txt", 'r')
total = 0
for line in infile:
    list = line.split()
    for word in list:
        num = int(word)
        total += num
print(total)
