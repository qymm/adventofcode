from functions import *
import math
from collections import defaultdict

def loadVectors (s):
    def parseLine (l):
        l = l.strip().split (" -> ")
        l1 = [ int(x) for x in l[0].split(",") ]
        l2 = [ int(x) for x in l[1].split(",") ]
        #print ((l1[0],l1[1]),(l2[0],l2[1]))
        return (l1[0],l1[1]),(l2[0],l2[1])
    li = []
    i = open(s).readlines()
    for line in i:
        li.append(parseLine(line))
    #print (li)
    return li

def drawOverlapsP1 (vec,overlaps):
    (x1,y1),(x2,y2) = vec
    #print (x1,y1,x2,y2)
    if (x1 == x2):
        for y in range(min(y1,y2),max(y1,y2)+1):
            overlaps[(x1,y)] += 1
    elif (y1 == y2):
        for x in range(min(x1,x2),max(x1,x2)+1):
            overlaps[(x,y1)] += 1

def drawOverlapsP2 (vec,overlaps):
    (x1,y1),(x2,y2) = vec
    #print (x1,y1,x2,y2)
    if (x1 == x2):
        for y in range(min(y1,y2),max(y1,y2)+1):
            #print ("New overlap at:",(x1,y))
            overlaps[(x1,y)] += 1
    elif (y1 == y2):
        for x in range(min(x1,x2),max(x1,x2)+1):
            #print ("New overlap at:",(x,y1))
            overlaps[(x,y1)] += 1
    else:
        xdir = 1 if x2 > x1 else -1
        ydir = 1 if y2 > y1 else -1
        curx = x1
        cury = y1
        while curx != x2 + xdir:
            overlaps[(curx,cury)] += 1
            curx += xdir
            cury += ydir
                
def isDiagonal (vec):
    if vec[0][0] == vec[1][0] or vec[0][1] == vec[1][1]:
        return 0
    else:
        return 1

if __name__ == "__main__":
    vectors = loadVectors("input5.txt")
    
    #print (vectors)

    # PART 1
    hvVec = []
    for vec in vectors:
        if not isDiagonal(vec):
            hvVec.append(vec)


    overlaps = defaultdict(int)
    for i in range(len(hvVec)):
            drawOverlapsP1(hvVec[i],overlaps)
            #print(overlaps)
    part1 = sum(o > 1 for o in overlaps.values())
    print (part1)


    #drawOverlapsP2(((290,366),(604,680)),overlaps)
    #drawOverlapsP2(((58,938),(718,278)),overlaps)
    #drawOverlapsP2(((75,252),(760,937)),overlaps)
    # PART 2
    overlaps = defaultdict(int)
    for i in range(len(vectors)):
            drawOverlapsP2(vectors[i],overlaps)
    part2 = sum(o > 1 for o in overlaps.values())
    print (part2)
