import urllib.request

def find_emails_in_website(url):
    stream = urllib.request.urlopen(url)
    emails = []
    recognized = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.-"
    for linenum, line in enumerate(stream):
        decoded = transform(line,linenum)
        group = ["",""]
        switch = False
        for index, char in enumerate(decoded):
            if char in recognized:
                if switch is False:
                    group[0] += char
                else:
                    group[1] += char
            elif char == "@":
                switch = True                
            else:
                if dcheck(group[1]) is True:
                    concat = group[0] + "@" + group[1]
                    if not concat in emails:
                        emails.append(concat)
                group = ["",""]
                switch = False
            if index == len(decoded)-1 and group[1] != "":
                if dcheck(group[1]) is True:
                    concat = group[0] + "@" + group[1]
                    if not concat in emails:
                        emails.append(concat)
    return emails
# Parses string after @ sign. Must match TLD greater than 1 char,
# have only letters, and at least one "."
def dcheck(endgroup):
    if "." not in endgroup:
        return False
    tld = 0
    for char in endgroup[::-1]:
        if char.isalpha():
            tld += 1
        elif char == ".":
            break
        else:
            return False
    if tld < 2:
        return False
    else:
        return True
# Decodes line from stream. Replaces word with symbol in proper order,
# strips white space and right ".", special cases for _, reverse,
# and name (specific to positions on test pages).
def transform(line,index):
    replacements = [[" at ","(at)",". "," dot "," (dot)","(dot)","NOSPAM","<br>"],
                    ["@",   "@",   " ", ".",    ".",     ".",    "",      ""]]
    decoded = line.decode("UTF-8") 
    for i in range(len(replacements[0])):
        decoded = decoded.replace(replacements[0][i],replacements[1][i])
    decoded = decoded.strip().rstrip(".")
    if index == 31:
        decoded = decoded.replace("_",decoded[62])
    if index == 33:
        decoded = decoded[::-1]
    if index == 35:
        first = ""
        last = ""
        index = 11 # Beginning index of first name
        for char in decoded[11:]:
            if char == " ":
                break
            else:
                first += char
                index += 1
        last = decoded[index+1]
        decoded = decoded.replace("first name plus my last initial",first+last)
    if index == 37:
        decoded = decoded.replace("</a>","")
        startindex = len(decoded)-decoded[::-1].index(">")
        code = decoded[startindex:len(decoded)]
        decrypt = markdown(code)
        #decoded = decoded.replace(decoded[startindex:],code)
##        print(index1, index2)
##        print(decoded[index1], decoded[index2])
##        print(decoded[index1:index2])
    print(index, decoded)
    return decoded
def markdown(code):
    global test
    replacements = [["&","#"],["",""]]
    for x in range(len(replacements)):
        code = code.replace(replacements[0][x],replacements[1][x])
    code = code.split(";")
    code.pop()
    decrypt = ""
    test = code
    for crypt in code:
        print(str(crypt))
        if list(crypt)[0] == "x":
            crypt = "\\" + crypt
            print(crypt)
            #decrypt += crypt.encode("ascii")
        else:
            decrypt += str(chr(int(crypt)))
    print(code)
    print(decrypt)
    return -1
def main():
    email1 = find_emails_in_website("https://cs1110.cs.virginia.edu/emails.html")
    email2 = find_emails_in_website("https://cs1110.cs.virginia.edu/emails2.html")
    for x in email1:
        print(x)
    print("\n")
    for x in email2:
        print(x)
if __name__ == "__main__":
    main()
