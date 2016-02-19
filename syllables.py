word = input("Please give me a word: ")
vowelCount = 0
consec = False
for letter in word:
    if letter in ['a','e','i','o','u','y']:
        vowelCount += 1
        if consec is True:
            vowelCount -= 1
        consec = True
    else:
        consec = False
    if letter == 'e' and letter == word[len(word)-1]:
        vowelCount -= 1
if vowelCount == 0:
    vowelCount = 1
print("The word " + word + " has " + str(vowelCount) + " syllables.")
