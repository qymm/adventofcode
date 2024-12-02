#https://adventofcode.com/2023/day/3

import sys
import string

if __name__ == "__main__":
    
    #with open("2023/input3.txt") as file:
    with open(sys.argv[1]) as file:
        lines = [l.rstrip() for l in file]

        pairs = []

        symbols = ""
        for line in lines:
            for c in line:
                if c != "." and not c.isnumeric() and c not in symbols:
                    print ("found:", c)
                    symbols = symbols + c
        print (symbols)

        def nearSymbol(num,iY):
            #print("\n")
            numLength = len(num[0])
            iX = num[1]
            segment = [line[max(0,iX-1):min(iX+numLength+1,len(line))] for line in lines[max(0,iY-1):min(iY+2,len(lines))]]
            #for row in segment:
            #    print(row)
            for row in segment:
                if any((symbol in symbols) for symbol in row):
                    return True
            return False

        part1 = 0
        part2 = 0

        for iY,line in enumerate(lines):
            for symbol in symbols:
                line = ".".join(line.split(symbol))
            tempNum = ""
            foundNum = False
            savedIndex = -1
            nums = []
            for index,c in enumerate(line):
                if c.isnumeric():
                    if not foundNum:
                        savedIndex = index
                        foundNum = True
                    tempNum = tempNum + c
                else:
                    if len(tempNum) > 0:
                        nums.append((tempNum,savedIndex))
                    tempNum = ""
                    foundNum = False
                    savedIndex = -1
            if len(tempNum) > 0:
                nums.append((tempNum,savedIndex))
            #print (nums)
            for num in nums:
                valid = nearSymbol(num,iY)
                #print(num[0],"Is near:",valid)
                if valid:
                    part1 = part1 + int(num[0])
        
        print(part1)

        def lookForGears(iX,iY,l):
            found = set()
            dirs = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
            for n in range(l):
                for dir in dirs:
                    dX, dY = dir
                    x = iX+dX+n
                    y = iY+dY
                    if x < 0 or x >= len(lines[0]):
                        continue
                    elif y < 0 or y >= len(lines):
                        continue
                    elif lines[iY+dY][iX+dX+n] == '*':
                        found.add((x,y))
            if found:
                return found
                    

        gears = {}
        for iY,line in enumerate(lines):
            temp = ""
            nums = []
            tempiX = -1
            for iX,c in enumerate(line):
                if c.isnumeric():
                    if temp == '':
                        tempiX = iX
                    temp += c
                else:
                    if temp != "":
                        nums.append ((tempiX,temp))
                        #print (nums)
                    temp = ''
                    tempiX = -1
            if temp != "" and tempiX != -1:
                nums.append((tempiX,temp))
            for num in nums:
                found = lookForGears(num[0],iY,len(num[1]))
                #print(num,found)
                if found:
                    for f in found:
                        if gears.get(f):
                            gears[f].append(num[1])
                        else:
                            gears[f] = [num[1]]
            print (gears)

        for gear in gears:
            if len(gears[gear]) == 2:
                #print (int(gears[gear][0]),"*",int(gears[gear][1]))
                part2 += int(gears[gear][0]) * int(gears[gear][1])

        print(part2)