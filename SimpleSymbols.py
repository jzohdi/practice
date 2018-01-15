
# Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence
# by either returning the string true or false. The str parameter will be composed of + and = symbols with several letters between them 
# (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. 
# So the string to the left would be false. The string will not be empty and will have at least one letter
#
#

def checkArray(myArray):
    for x in range(len(myArray)):
        if myArray[0].isalpha():
            return False
        if myArray[(len(myArray) - 1)].isalpha():
            return False
        
        if myArray[x].isalpha():
            if myArray[x-1] == '+' and myArray[x+1] == '+':
                return True
            if myArray[x-1] != '+' or myArray[x+1] != '+':
                return False


def SimpleSymbols(str):
    
    newArray = []
    for i in range(len(str)):
        newArray.append(str[i])
    
    if checkArray(newArray):
        return 'true'
    if not checkArray(newArray):
        return 'false'

print SimpleSymbols(raw_input())
