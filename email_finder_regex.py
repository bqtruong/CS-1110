import urllib.request
import codecs
import re

def find_emails_in_website(url):
    stream = urllib.request.urlopen(url)
    emails = []
    reg = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]{2,})"
    regex = re.compile(reg)
    for linenum, line in enumerate(stream):
        decoded = transform(line,linenum)
        emails += regex.findall(decoded)
    noduplicates = []
    for email in emails:
        if email not in noduplicates:
            noduplicates.append(email)
    return noduplicates
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
    if index == 31: # Underscore
        decoded = decoded.replace("_",decoded[62])
    if index == 33: # Reverse
        decoded = decoded[::-1]
    if index == 35: # First, Last initial
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
    if index == 37: # Markdown
        decoded = decoded.replace("</a>","")
        startindex = len(decoded)-decoded[::-1].index(">")
        code = decoded[startindex:len(decoded)]
        decrypt = markdown(code)
        delindex = decoded.index("<")
        decoded = decoded.replace(decoded[delindex:],decrypt)
    return decoded
# Converts Markdown's email obfuscation to ASCII
def markdown(code):
    replacements = [["&","#"],["",""]]
    for x in range(len(replacements)):
        code = code.replace(replacements[0][x],replacements[1][x])
    code = code.split(";")
    code.pop()
    decrypt = ""
    for crypt in code:
        if list(crypt)[0] == "x":
            decrypt += str(codecs.decode(crypt[1:], "hex").decode("UTF-8"))
        else:
            decrypt += str(chr(int(crypt)))
    return decrypt
def main():
    email1 = find_emails_in_website("https://cs1110.cs.virginia.edu/emails.html")
    email2 = find_emails_in_website("https://cs1110.cs.virginia.edu/emails2.html")
    for x in email1:
        print(x)
    print("")
    for x in email2:
        print(x)
if __name__ == "__main__":
    main()
