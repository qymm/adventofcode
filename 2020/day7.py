from file_in import load
from datetime import datetime

def processInput(l):
    l = load(l)

    lines = []
    for n in l:
        lines.append(n.strip("\n"))
    return lines

def createRules(input):
    rules = []
    for line in input:
        if line.find("no other bags") == -1:
            n = line.split(" bags contain ")
            bag = n[0]
            insideBag = n[1].split (", ")
            for y, x in enumerate(insideBag):
                insideBag[y] = insideBag[y].strip('.')
            rules.append ((bag,insideBag))
        else:
            n = line.split(" bags contain ")
            bag = n[0]
            rules.append ((bag,[]))
    return rules

def findRule(input):
    temp = input.lstrip("1234567890 ").rstrip(" bags")
    for y in rules:
        if y[0].find(temp) != -1:
            return y
    assert y == 0, "findRule() returned nothing."


def hasShinyGold(input):
    #print (":" + spaces + "hasShinyGold(input: " + input[0] + ")")

    for y in hasGold:
        if y[0] == input[0] and y[1]:   
            #print ("SKIPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
            return 1
        elif y[0] == input[0] and not y[1]:
            #print ("SKIPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
            return 0

    if len(input[1]) == 0:
            hasGold.append ((input[0], False))
            return 0
    else:
        for y in input[1]:
            if y.find("shiny gold") != -1:
                hasGold.append ((input[0], True))    
                return 1
            else:
                nextRule = findRule(y)
                if hasShinyGold(nextRule) == 1:
                    hasGold.append ((input[0], True))                        
                    return 1               
        return 0

def countMeAndInside(input):
    if len(input[1]) == 0:
        return 1
    else:
        insideCount = 0
        yCount = 0
        for y in input[1]:
            yCount = int(y.split(" ")[0])
            insideCount += yCount * countMeAndInside(findRule(y))
        return (1 + insideCount)

if __name__ == "__main__":

    i = processInput("input7.txt")

    global rules
    rules = createRules(i)
    for y in rules:
        print (y)

    global hasGold
    hasGold = []

    count = 0
    start = datetime.utcnow()
    print ("Starting gold bag count at: " + str(start))
    for y in rules:
        #print ("Checking: " + y[0])
        if hasShinyGold(y) == 1:
            count += 1
    print (count)
    finish = datetime.utcnow()
    print ("Found at: " + str(finish))
    print(' '.join(('total time:', str(finish-start))))

    count = countMeAndInside(findRule("shiny gold")) - 1
    print (count)