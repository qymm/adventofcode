#https://adventofcode.com/2024/day/4

import sys
import string
import re

if __name__ == "__main__":

    with open(sys.argv[1]) as file:
        grid = [l.rstrip() for l in file]
        n = len(grid) # vertical length of grid
        diags = []
        for d in range(n*2-1): # saving top-left to bottom-right
            row = max(0, d - n + 1)
            col = max(0, n - 1 - d)
            diag = []
            while row < n and col < n:
                diag.append(grid[row][col])
                row+=1
                col+=1
            diags.append(''.join(diag))
        
        for d in range(n*2-1): # saving top-right to bottom-left
            row = max(0, d - n + 1)
            col = min(n - 1, d)
            diag = []
            while row < n and col >= 0:
                diag.append(grid[row][col])
                row+=1
                col-=1
            diags.append(''.join(diag))

        #diags = "".join(diags)
        print(diags)

        verts = [] # saving vertical lines
        for d in range(n):
            row = 0
            col = d
            vline = []
            while row < n:
                vline.append(grid[row][col])
                row+=1
            verts.append(''.join(vline))
        print(verts)

        p1 = 0
        lines = grid + diags + verts
        for l in lines:
            p1 += len(re.findall('XMAS',l))
            p1 += len(re.findall('SAMX',l))
        print (p1)

        # -----------

        def checkPos (pos):
            y,x = pos
            i = grid[y-1][x-1] + grid[y+1][x+1]
            j = grid[y-1][x+1] + grid[y+1][x-1]
            if i == "MS" or i == "SM":
                if j == "MS" or j == "SM":
                    return True
                else:
                    return False
            else:
                return False

        p2 = 0
        positions = []
        for y,line in enumerate(grid):
            for x,char in enumerate(line):
                if char == 'A' and y > 0 and x > 0 and x < len(line)-1 and y < len(grid)-1:
                    positions.append((y,x))
        for pos in positions:
            if checkPos(pos):
                p2 += 1
        print (p2)