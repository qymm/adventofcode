import string

def load(s):
    with open(s) as input:
        return(input.readlines())

def load_ints(file):
    o = []
    for n in load(file):
        o.append(int(n))
    return o

def checkHex(input):
    for letter in input:
        if letter not in string.hexdigits:
            return False
    return True