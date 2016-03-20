##number = input("Type a credit card number (just digits): ")
##number = [int(x) for x in number]
##check1 = sum(number[::2]) if len(number) % 2 == 1 else sum(number[1::2])
###check2 = sum(number[::2]*2) if len(number) % 2 == 0 else sum(number[1::2]*2)
##check2 = 0
##if len(number) % 2 == 0:
##    check2 = [x*2 for x in number[::2]]
##else:
##    check2 = [x*2 for x in number[1::2]]
##check2 = "".join(str(x) for x in check2)
##check2 = [int(x) for x in check2]
##check2 = sum(check2)
##if (check1 + check2) % 10 == 0:
##    print("Yes, " + "".join(str(x) for x in number) + " is a valid credit card number")
##else:
##    print("".join(str(x) for x in number) + " is not a valid credit card number")

l = 'test'
k = ['1','2','3']
for x in range(len(k)):
    l += k[x]
