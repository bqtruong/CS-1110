cipher = input("Enter your cipher text: ")
letterMap = "abcdefghijklmnopqrstuvwxyz"
cipher = [letter.lower() for letter in cipher]
print("The decoded phrase is: ", end = "")
for letter in cipher:
    if letter.isalpha():
        print(letterMap[(letterMap.index(letter) - 3) % 26], end = "")
    else:
        print(letter, end = "")
