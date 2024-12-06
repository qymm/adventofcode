#https://adventofcode.com/2024/day/6

import sys
import string

guards = "<^>v"
movementDict = {
    "<": (-1,0),
    "^": (0,-1),
    ">": (1,0),
    "v": (0,1)
}

if __name__ == "__main__":

    with open(sys.argv[1]) as file:
        grid = [l.rstrip() for l in file]
        backupgrid = grid.copy() # saving initial condition
        xgrid = grid.copy() # grid upon which we store valid positions to place an obstacle

        def getStartingGuardPos(grid): # given a grid, find the guard's position and return the traditional tuple (guard direction, (guardx, guardy))
            for y,row in enumerate(grid):
                for guard in guards:
                    x = row.find(guard)
                    if x != -1:
                        #print("Guard: [", x,y, "]")
                        guardPos = (guard,(x,y))
                        return guardPos

        guardPos = getStartingGuardPos(grid) # starting off

        def getCurrentPos(): # this used to be a function, but P2 made me change its behavior to just be a getter
            return guardPos

        def exitCondition(pos): # given a guard position, e.g. ("^",(0,1)), is the grid in a condition where the guard is at the edge of the screen and going to leave?
            guard = pos[0]
            x,y = pos[1]
            if x == 0 and guard == "<":
                return True
            elif x == len(grid[0])-1 and guard == ">":
                return True
            elif y == 0 and guard == "^":
                return True
            elif y == len(grid)-1 and guard == "v":
                return True
            else:
                return False
        
        def prettyPrint(grid): # to see the grid without list printing accoutrement
            for row in grid:
                print (row)
            print ("\n")
        
        def traverse(): # do a move!
            guard, (x,y) = getCurrentPos()
            (x2,y2) = (x+movementDict[guard][0],y+movementDict[guard][1]) #get x2,y2, in the direction the guard is pointing
            #print(x2,y2)
            if grid[y2][x2] == guard: #if the guard is ever retracing its steps, loop found
                print("Loop found.")
                return ("@",(-1,-1)) # return a nonsense character
            if grid[y2][x2] == "#": # otherwise, if the next step is an obstacle, spin the guard
                if guard == "^":
                    guard = ">"
                elif guard == ">":
                    guard = "v"
                elif guard == "v":
                    guard = "<"
                elif guard == "<":
                    guard = "^"
                else:
                    print ("weird guard")
                grid[y] = grid[y][:x] + guard + grid [y][x + 1:]
                guardPos = guard,(x,y)
            else: # otherwise, step the guard forward, then place an old copy of itself behind. Also, place an X on the xgrid.
                grid[y2] = grid[y2][:x2] + guard + grid[y2][x2 + 1:]
                grid[y] = grid[y][:x] + guard + grid [y][x + 1:]
                xgrid[y] = xgrid[y][:x] + "X" + xgrid [y][x + 1:]
                guardPos = guard,(x2,y2)
            #print (guardPos)
            #prettyPrint(grid)
            return guardPos
        
        # - START PART 1 -

        while not exitCondition(getCurrentPos()):
            guardPos = traverse()

        for idy,row in enumerate(grid):
            for idx,char in enumerate(row):
                if char in guards:
                    xgrid[idy] = xgrid[idy][:idx] + "X" + xgrid [idy][idx + 1:]

        p1 = 0
        for row in xgrid:
            p1 += row.count("X")
        print (p1)

        # - START PART 2 -

        grid = backupgrid.copy() # reload the grid. we still have the xgrid

        p2 = 0
        for idy,row in enumerate(xgrid):
            xpos = [i for i, char in enumerate(row) if char == "X"]
            #print (xpos, "positions to check")
            loopFound = False
            for idx in xpos: # for each X in the X grid...
                loopFound = False
                testGrid = backupgrid.copy()
                testGrid[idy] = testGrid[idy][:idx] + "#" + testGrid[idy][idx + 1:] # test replacing with an obstacle
                
                backupGuard,(backupX,backupY) = getStartingGuardPos(backupgrid) # replace the guard if we have accidentally replaced him
                testGrid[backupY] = testGrid[backupY][:backupX] + backupGuard + testGrid[backupY][backupX + 1:]

                grid = testGrid.copy()
                guardPos = getStartingGuardPos(grid)
                traversal = 0
                while not exitCondition(getCurrentPos()): # and run traversal
                    guardPos = traverse()
                    traversal += 1
                    #print(traversal)
                    if guardPos[0] == "@" or traversal > 9999: # if guardpos is nonsense, we have detected a loop! if traversal exceeds 9999, we have (likely...) run into an infinite loop that we do not (know how to) detect
                        loopFound = True
                        p2 += 1
                        break
                if loopFound:
                    pass
                else:
                    print("Full traversal, carry on.")
                        
        print(p2)