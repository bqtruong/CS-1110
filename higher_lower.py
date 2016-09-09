import random
num = int(input("What should the answer be? "))
if num == -1:
    num = random.randint(1,100)
counter = 0
win = False
while counter < 5 and win == False:
    guess = int(input("Guess a number: "))
    if guess == num:
        win = True
    elif guess > num and counter != 4:
        print("The number is lower than that.")
    elif guess < num and counter != 4:
        print("The number is higher than that.")
    counter += 1
if win == True:
    print("You win!")
else:
    print("You lose; the number was " + str(num) + ".")
