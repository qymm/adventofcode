#https://adventofcode.com/2022/day/12

import sys
import math
import operator
import string
from enum import Enum

# map[y][x]

if __name__ == "__main__":
    grid = []
    end = (-1,-1)
    start = (-1,-1)

    Dir = {
        "LEFT": (0,-1),
        "RIGHT": (0,1),
        "UP": (-1,0),
        "DOWN": (1,0),
        "SELF": (0,0),
    }

    def getCell(pos,dir):
        if (pos[0]+Dir.get(dir)[0] >= 0 and pos[1]+Dir.get(dir)[1] >= 0):
            return grid[pos[0]+Dir.get(dir)[0]][pos[1]+Dir.get(dir)[1]]
        else:
            return "#"

    def FindNext(pos,next,moves):
        print("starting find next at",pos,next,moves)
        char = getCell(pos,"SELF")
        if char == "S":
            next += "ab"
        else:
            next += chr(ord(char)+1)
        moveFound = False
        while not moveFound:
            if getCell(pos,"LEFT") in next:
                moves.append(FindNext((pos[0]+Dir.get("LEFT")[0],pos[1]+Dir.get("LEFT")[1]),next,[]))
            elif getCell(pos,"RIGHT") in next:
                moves.append(FindNext((pos[0]+Dir.get("RIGHT")[0],pos[1]+Dir.get("RIGHT")[1]),next,[]))
            elif getCell(pos,"UP") in next:
                moves.append(FindNext((pos[0]+Dir.get("UP")[0],pos[1]+Dir.get("UP")[1]),next,[]))
            elif getCell(pos,"DOWN") in next:
                moves.append(FindNext((pos[0]+Dir.get("DOWN")[0],pos[1]+Dir.get("DOWN")[1]),next,[]))
            else:
                return []
            if len(moves) > 0:
                print ("Found something")
                moveFound = True
        return moves



    with open(sys.argv[1]) as file:
        for j,line in enumerate(file):
            grid.append([i for i in line.strip()])
            if "E" in line:
                end = (j,line.find("E"))
                #print(end)
            if "S" in line:
                start = (j,line.find("S"))
                #print(start)
        #print(grid)
        print(FindNext(start,"",[]))