numbers = input("Numbers: ").split()
#numbers = ['4', '9', '2', '3', '5', '7', '8', '1', '6']
numbers = [int(n) for n in numbers]
numList = [numbers[0:3], numbers[3:6], numbers[6:9]]
numList += zip(numList[0], numList[1], numList[2])
numList += [numbers[0::4], numbers[2:7:2]]
sumList = [sum(x) for x in numList]
valid = True
for x in range(len(sumList)):
    if sumList[x] != 15:
        valid = False
        if x in range(0,3):
            print("Row ", end="")
        elif x in range(3,6):
            print("Column ", end="")
        elif x in range(6,8):
            print("Diagonal ", end="")
        print(str(x % 3 + 1) + " fails the test!")
if valid:
    print("This is a valid Lo Shu Magic Square!")
else:
    print("This is not a Lo Shu Magic Square!")
