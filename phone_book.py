book = []
for x in range(5):
    book.append(input("Add an entry to the phone book: "))
names = []
numbers = []
for line in book:
    names.append(''.join([char for char in line if char.isalpha()]))
    numbers.append(''.join([char for char in line if (char.isnumeric() or char == '-')]))
name = input("Who do you want to call?: ")
if names.count(name) > 0:
    print(name + "'s number is: " + numbers[names.index(name)])
else:
    print("That name is not the phone book.")
number = input("Which number do you want to lookup?: ")
if numbers.count(number) > 0:
    print("That number belongs to: " + names[numbers.index(number)])
else:
    print("That number is not the phone book.")
