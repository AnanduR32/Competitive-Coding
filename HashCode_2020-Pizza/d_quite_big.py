fileOutput = open("output_d_quite_big.in", "w")

with open('d_quite_big.in') as fileInput:
    maxSlice, pizzaTypes = [int(x) for x in next(fileInput).split()]
    sliceList = [int(x) for x in next(fileInput).split()]
    
listLength = len(sliceList)
count = 0
pos = []

for slice in reversed(sliceList):
    if(slice <= maxSlice):
        pos.append(listLength-1)
        count += 1
        maxSlice -= slice
    listLength -= 1

print(count)
print(' '.join(map(str, sorted(pos))))
fileOutput.write(str(count) + "\n")
fileOutput.writelines(' '.join(map(str, sorted(pos))))

fileInput.close()
fileOutput.close()
