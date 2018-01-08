# change the letters in a given string to the next letter in the alphabet. if resulting letter is a vowel, capitalize it.
def LetterChanges(str):
    newstr = "";
    for i, c in enumerate(str):
        if c.isalpha():
            if c =='z':
                newstr += 'a'
            elif c == 'Z':
                newstr += 'A'
            else:
                newstr += chr(ord(c) + 1)
        else:
            newstr += c
    finalstr = ""
    for x, y in enumerate(newstr):
        if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u':
            finalstr += y.upper()
        else:
            finalstr += y

    print("Output: " + finalstr)

print("Input: ", end = "")

string = str(input())

LetterChanges(string)
