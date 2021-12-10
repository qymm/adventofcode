import math

def load(s):
    i = []
    with open(s) as file:
        i = [ line.strip() for line in file.readlines() ]
    #print(i)
    return i

def openToClose(o,opens,closes):
    return (closes[opens.index(o)])

if __name__ == "__main__":
    lines = load("input10.txt")
    p2lines = []
    opens = ["(","[","{","<"]
    closes = [")","]","}",">"]
    p1scores = [3,57,1197,25137]
    p2scores = [1,2,3,4]
    illegalChars = []
    
    #PART 1
    for lineIdx,line in enumerate(lines):
        openingString = []
        corrupt = False
        for idx,c in enumerate(line):
            if c in opens:
                #save a string of currently open brackets
                openingString.append(c)
            elif c in closes:
                #if it closes with the wrong bracket, save it and mark as corrupt
                if opens[closes.index(c)] != openingString[-1]:
                    #print ("Found corruption in line",lineIdx,c)
                    illegalChars.append(c)
                    corrupt = True
                    break
                #if it closes properly, remove the latest char from the openingString
                else:
                    openingString.pop()
        if not corrupt:
            #A LITTLE SNEAKY PART 2 IN HERE
            #If not corrupt, save openingString in reverse into our Part 2 list.
            openingString.reverse()
            p2lines.append(openingString)
        #print ("Line",lineIdx,"done.")

    score = 0
    for c in illegalChars:
        score += p1scores[closes.index(c)]
    print ("PART 1:",score)

    newLines = []
    #I wanted to solve it faster than I could remember how to map this.
    for line in p2lines:
        newLine = []
        for c in line:
            newLine.append(openToClose(c,opens,closes))
        newLines.append(newLine)
    p2lines = newLines
    
    lineScores = []
    for line in p2lines:
        score = 0
        for c in line:
            score *= 5
            score += p2scores[closes.index(c)]
        lineScores.append(score)
    lineScores.sort()
    #print(lineScores)
    print("PART 2:", lineScores[math.floor(len(lineScores)/2)])