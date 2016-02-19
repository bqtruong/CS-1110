word = list(input("Enter a word: ").upper())
hidden = ["-" for x in range(len(word))]
guessCounter = 6
done = False
while not done:
    guess = input("[" + "".join(hidden) + "] You have " + str(guessCounter) + " left, enter a letter: ").upper()
    if guess in word:
        print("Correct!")
        for x in range(len(word)):
            if word[x] == guess:
                hidden[x] = guess
    else:
        print("Incorrect!")
        guessCounter -= 1
        if guessCounter == 0:
            print("You lose! The word was \"" + "".join(word) + "\"")
            done = True
    if "-" not in hidden:
        print("You win! The word was \"" + "".join(word) + "\"")
        done = True
