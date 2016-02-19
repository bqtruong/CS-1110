print("The Game of Nim\n")
marbles = int(input("Number of marbles are in the pile: "))
dynamicPower = [pow(2,x)-1 for x in range(0,marbles) if pow(2,x)-1 < marbles]
starter = input("Who will start? (p or c): ")
lastPlayer = str(starter)
while marbles > 0:
    print("The pile has " + str(marbles) + " marbles in it.")
    if lastPlayer == "p":
        take = marbles
        if marbles // 2 == 0:
            take = int(input("How many marbles do you want to take? (1-1): "))
        else:
            while not take >= 1 or not take <= (marbles // 2):
                take = int(input("How many marbles do you want to take? (1-" + str(marbles//2) + "): "))
        marbles -= take
        lastPlayer = "c"
    else:
        take = marbles // 2
        if marbles in dynamicPower:
            take = 1
        else:
            while (marbles - take) not in dynamicPower:
                take -= 1
        marbles -= take
        print("The computer takes " + str(take) + " marbles.")
        lastPlayer = "p"
if lastPlayer == "p":
    print("The player wins!")
else:
    print("The computer wins!")
