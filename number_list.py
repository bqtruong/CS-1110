numList = []
for x in range(5):
    numList.append(int(input("Number " + str(x+1) + ": ")))
print("You entered: " + str(numList))
avg = 0
for x in numList:
    avg += int(x)
avg = avg / len(numList)
print("The average is: " + str(avg))
print("The range is: " + str(len(numList)))
rem = int(input("Which item do you want to remove?: "))
del numList[numList.index(rem)]
print("The new list has the following values: " + str(numList))
avg = 0
for x in numList:
    avg += int(x)
avg = avg / len(numList)
print("The average is: " + str(avg))
print("The range is: " + str(len(numList)))
