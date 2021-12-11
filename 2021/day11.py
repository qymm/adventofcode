import math

def loadGrid(s):
    grid = []
    with open(s) as file:
        for line in file.readlines():
            row = []
            for c in line.strip() :
                row.append(int(c))
            grid.append(row)
    return grid

def printGrid(grid):
    print ( "-" * len(grid[0]))
    for row in grid:
        for c in row:
            print (c, " ", end = '')
        print()
    print ( "-" * len(grid[0]))

def flash(grid,flashCounter,r,c):

    #Clamping.
    lowerRow = r-(r>0)
    upperRow = r+1+((r+1)<len(grid))
    lowerCol = c-(c>0)
    upperCol = c+1+((c+1)<len(grid[0]))

    #Increase all neighboring squid.
    for row in range(lowerRow,upperRow):
        for col in range(lowerCol,upperCol):
            if (row,col) != (r,c):
                grid[row][col] += 1

    #Find charged neighboring squid, then flash.
    for row in range(lowerRow,upperRow):
        for col in range(lowerCol,upperCol):
            if (row,col) != (r,c):
                if grid[row][col] > 9 and flashCounter[row][col] != 1:
                    flashCounter[row][col] = 1
                    flash(grid,flashCounter,row,col)

def step(grid):
    #flashCounter tracks how many squid have flashed this turn, as well as making sure they don't double flash.
    flashCounter = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    #Increase all squid.
    for r,line in enumerate(grid):
        for c,squid in enumerate(line):
            grid[r][c] += 1

    #Find charged squid, then flash.
    for r,line in enumerate(grid):        
        for c,squid in enumerate(line):
            if squid > 9 and flashCounter[r][c] != 1:
                flashCounter[r][c] = 1
                flash(grid,flashCounter,r,c)
                #print("flashing")

    #Reset flashed squid.
    for r,line in enumerate(grid):
        for c,squid in enumerate(line):
            if flashCounter[r][c] >= 1:
                grid[r][c] = 0

    printGrid(grid)
    return sum(map(sum,flashCounter))

if __name__ == "__main__":

    #PART 1
    grid = loadGrid("input11.txt")
    printGrid(grid)
    flashCount = 0

    #Find how many flashes happen in 100 steps.
    for n in range(100):
        print("STEP", n+1)
        flashCount += step(grid)
        print (flashCount)

    #PART 2
    grid = loadGrid("input11.txt")
    stepCount = 0

    #Step until 100 squid flash on the same step.
    while flashCount != 100:
        stepCount += 1
        print("STEP", stepCount)
        flashCount = step(grid)
        if flashCount == 100:
            print("ENDED ON STEP", stepCount)