#https://adventofcode.com/2022/day/8

import sys

if __name__ == "__main__":

    def printGrid(grid):
        print ( "-" * len(grid[0]))
        for row in grid:
            for c in row:
                print (c, "", end = '')
            print()
        print ( "-" * len(grid[0]))

    with open(sys.argv[1]) as file:

        trees = []

        for x, line in enumerate(file):
            trees.append(list(line.strip()))
        #printGrid(trees)
        gridX = len(trees[0])
        gridY = len(trees)
        #print("gridsize:",gridX,gridY)

        visibility = [[0 for i in range(gridY)] for j in range(gridX)]

        # REMEMBER IT'S TREES[COL][ROW]

        for y,row in enumerate(trees):
            for x,tree in enumerate(row):
                #print ("("+str(x)+","+str(y)+")",tree)
                visibility[y][x] = 0
                if y == 0 or x == 0 or y == gridY-1 or x == gridX-1:
                    #print("defaultly visible")
                    visibility[y][x] = 1
                elif len([i for i in range(x+1,gridX) if trees[y][i] >= tree]) == 0:
                    #print("visible right")
                    visibility[y][x] = 1
                elif len([i for i in range(0,x) if trees[y][i] >= tree]) == 0:
                    #print("visible left")                   
                    visibility[y][x] = 1
                elif len([j for j in range(y+1,gridY) if trees[j][x] >= tree]) == 0:
                    #print("visible down")   
                    visibility[y][x] = 1
                elif len([j for j in range(0,y) if trees[j][x] >= tree]) == 0:
                    #print("visible up")   
                    visibility[y][x] = 1

        #printGrid(visibility)

        print(sum([sum(x) for x in visibility])) #P1

        scores = [[0 for i in range(gridY)] for j in range(gridX)]

        def trimView(view,height):
            for n,i in enumerate(view):
                if i >= int(height):
                    return view [0:n+1]
            return view

        highest = 0

        for y,row in enumerate(trees):
            for x,tree in enumerate(row):
                #print("(",x,y,")",":",tree)
                rightView = [int(trees[y][i]) for i in range(x+1,gridX)]
                rightView = trimView(rightView,tree)

                leftView = [int(trees[y][i]) for i in range(0,x)]
                leftView.reverse()
                leftView = trimView(leftView,tree)

                #print("right",rightView)
                #print("left",leftView)

                upView = [int(trees[j][x]) for j in range(0,y)]
                upView.reverse()
                upView = trimView(upView,tree)

                downView = [int(trees[j][x]) for j in range(y+1,gridY)]
                downView = trimView(downView,tree)

                #print("up",upView)
                #print("down",downView)

                score = len(rightView)*len(leftView)*len(upView)*len(downView)

                if highest < score:
                    highest = score

        print(highest) #P2