from file_in import load
#from enum import Enum
import math

#N E S W
#0 1 2 3

currentDirection = 1
currentPos = (0,0)
wayPos = (10, -1)

def processInput(l):
    l = load(l)

    rows = []
    for n in l:
        direction = ''.join ([i for i in n if not i.isdigit()]).strip("\n")
        length = int(''.join ([i for i in n if i.isdigit()]).strip("\n"))
        rows.append ((direction,length))
    return rows

def goBoatGo(tuple):
    global currentDirection
    global currentPos
    direction = tuple[0]
    length = tuple[1]

    def pushBoat(direc):
        global currentPos
        if direc == 0:
            currentPos = (currentPos[0], currentPos[1]-length)
        elif direc == 1:
            currentPos = (currentPos[0]+length, currentPos[1])
        elif direc == 2:
            currentPos = (currentPos[0], currentPos[1]+length)
        elif direc == 3:
            currentPos = (currentPos[0]-length, currentPos[1])
        print (currentPos)

    if direction == 'L' or direction == 'R':
        if direction == 'L':
            currentDirection -= length/90
            currentDirection = correctDir(currentDirection)
        elif direction == 'R':
            currentDirection += length/90
            currentDirection = correctDir(currentDirection)
    elif direction == 'F':
            currentDirection = currentDirection
            pushBoat(currentDirection)
    elif direction == 'N':
        pushBoat(0)
    elif direction == 'E':
        pushBoat(1)
    elif direction == 'S':
        pushBoat(2)
    elif direction == 'W':
        pushBoat(3)

def goWaypointGo(tuple):
    global currentDirection
    global currentPos
    global wayPos
    direction = tuple[0]
    length = tuple[1]

    def rotate(direc,tuple):
        if direc:
            tempTuple = (tuple[1]*-1, tuple[0])
        else:
            tempTuple = (tuple[1], tuple[0]*-1)
        return tempTuple

    #moveTheBoat
    if direction == 'F':
        tempX = wayPos[0]*length
        tempY = wayPos[1]*length
        currentPos = (currentPos[0]+tempX, currentPos[1]+tempY)
        print ("Boat moved by: " + str((tempX, tempY)) + " new loc: " + str(currentPos))
    #waypoint rotating
    elif direction == 'L' or direction == 'R':
        for x in range (0, int(length/90)):
            if direction == 'L':
                wayPos = rotate(0,wayPos)
            if direction == 'R':
                wayPos = rotate(1,wayPos)
    #waypoint pushing
    elif direction == 'N':
        wayPos = (wayPos[0], wayPos[1]-length)
    elif direction == 'E':
        wayPos = (wayPos[0]+length, wayPos[1])
    elif direction == 'S':
        wayPos = (wayPos[0], wayPos[1]+length)
    elif direction == 'W':
        wayPos = (wayPos[0]-length, wayPos[1])


def correctDir (temp):
    while temp > 3 or temp < 0:
        if temp > 3:
            temp -= 4
        if temp < 0:
            temp += 4
    return temp

def calcManhattan (pos1, pos2):
    tempY = abs(pos2[0]) - abs(pos1[0])
    tempX = abs(pos2[1]) - abs(pos1[1])
    return tempY + tempX

if __name__ == "__main__":
    
    i = processInput ("input12.txt")
    #print (i)

    for line in i:
         goWaypointGo(line)

    distance = calcManhattan((0,0),currentPos)
    print ("Manhattan distance: " + str(distance))