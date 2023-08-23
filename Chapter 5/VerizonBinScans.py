file = open("VerizonBinScans.txt", 'r')
assetList = []
for line in file:
    line = line.strip()
    assetList.append(line)
file.close()
file = open("VerizonBinScans_2.txt", 'w')
file.write("Sorted List: \n")
sortedList = []

for values in assetList:
    sortedList.append(int(values[-6:]))
sortedList.sort()
for values in sortedList:
    file.write(str(values) + '\n')
file.close()
print(sortedList)
print("number of items in bin: ", len(sortedList))
print(__file__)
