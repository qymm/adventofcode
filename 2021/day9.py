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
            print (c, end = '')
        print()
    print ( "-" * len(grid[0]))

def findLows(grid):
    def neighbors (grid, r, c):
        n = sum((row[c-(c>0):c+2] for row in grid[r-(r>0):r+2]),[])
        n.remove(grid[r][c])
        return n
    lows = []
    lowPoints = []
    for rowIdx,row in enumerate(grid):
        for colIdx,col in enumerate(row):
            searchCells = neighbors(grid,rowIdx,colIdx)
            #print(searchCells)
            if all(grid[rowIdx][colIdx] < x for x in searchCells):
                #print ("Found low:", grid[rowIdx][colIdx])
                lows.append(grid[rowIdx][colIdx])
                lowPoints.append ((rowIdx,colIdx))
    return lows, lowPoints

def findArea(grid,r,c):
    def recurse(grid,paintGrid,r,c):
        #print ("Recursing", (r,c), grid[r][c])
        for rowIdx in range(r-(r>0),r+1+((r+1)<len(grid))):
            if (r,c) != (rowIdx,c) and grid[rowIdx][c] > grid[r][c] and grid[rowIdx][c] != 9:
                recurse(grid,paintGrid,rowIdx,c)
        for colIdx in range (c-(c>0),c+1+((c+1)<len(grid[0]))):
            if (r,c) != (r,colIdx) and grid[r][colIdx] > grid[r][c] and grid[r][colIdx] != 9:
                recurse(grid,paintGrid,r,colIdx)
        paintGrid[r][c] = 1
        #print ("Backing up.")
        
    paintGrid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    recurse(grid,paintGrid,r,c)
    #printGrid(paintGrid)
    return sum(map(sum,paintGrid))

if __name__ == "__main__":
    grid = loadGrid("input9.txt")

    #SOLVE PART 1
    lows, lowPoints = findLows(grid)
    riskLevel = 0
    for low in lows:
        riskLevel += low+1
    print ("PART 1 RISK LEVEL:", riskLevel)

    #SOLVE PART 2
    areas = []
    for lowPoint in lowPoints:
        area = findArea(grid,lowPoint[0],lowPoint[1])
        #print("Basin area:", area)
        areas.append(area)
    areas.sort()
    print("THREE BIGGEST BASINS:", areas[-3:])
    print("PART 2 PRODUCT:",math.prod(areas[-3:]))