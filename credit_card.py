number = input("Type a credit card number (just digits): ")
number = [int(x) for x in number]
check1 = sum(number[::2]) if len(number) % 2 == 1 else sum(number[1::2])
check2 = sum(number[::2]*2) if len(number) % 2 == 0 else sum(number[1::2]*2)
if (check1 + check2) % 10 == 0:
    print("Yes, " + "".join(str(x) for x in number) + " is a valid credit card number")
else:
    print("".join(str(x) for x in number) + " is not a valid credit card number")
