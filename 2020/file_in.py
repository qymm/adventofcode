import string

def load(s):
    with open(s) as input:
        return(input.readlines())

def checkHex(input):
    for letter in input:
        if letter not in string.hexdigits:
            return False
    return True

def withinBounds (int, lower, upper):
    return ( int >= lower and int <= upper )

def nicePrint (rows):
    for row in rows:
        print (row)   
    print ("\n")        