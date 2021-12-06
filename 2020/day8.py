from file_in import load
from datetime import datetime

def processInput(l):
    l = load(l)

    lines = []
    for n in enumerate(l):
        lines.append((n[0],n[1].strip("\n")))
    return lines

def handleLine(line):

    global accCount
    global flag
    global iteration
    ins =  line[1][0:3]
    step = int(line[1][4:])
    next = 0

    if line[0] in used:
        print (str(line[0]) + " is a repeat. Ending.")
        return -1
    else:
        used.append (line[0])

    if ins == "acc":
        accCount += step
        next = line[0] + 1
    elif ins == "jmp":
        if flag == False and line[0] not in iteration:
            print ("Swapping " + str(line[0]) + " jmp to nop")
            flag = True
            next = line[0] + 1
            iteration.append (line[0])
        else:
            next = line[0] + step

    elif ins == "nop":
        if flag == False and line[0] not in iteration:
            print ("Swapping " + str(line[0]) + " nop to jmp")
            flag = True
            next = line[0] + step
            iteration.append (line[0])
        else:
            next = line[0] + 1

    #print ("Executed: " + ins + " " + str(step) + ", going to " + str(next))
    return next

if __name__ == "__main__":

    global accCount
    global used
    global iteration
    global flag
    used = []
    accCount = 0
    
    i = processInput ("input8.txt")
    currentIndex = 0
    used.append (currentIndex)
    while currentIndex != -1:
        currentIndex = handleLine (i[currentIndex])
    print (accCount)

    iteration = []
    while 1:
        used = []
        accCount = 0
        currentIndex = 0
        flag = False
        while currentIndex != -1 and currentIndex < len(i):
            currentIndex = handleLine (i[currentIndex])
        if currentIndex >= len(i):
            break
        print (iteration)
    print ("FOUND IT: " + str(accCount))
        