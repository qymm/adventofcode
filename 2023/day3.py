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

        def isGear(gearLoc):
            idx, idy = gearLoc
            #print("checking",idx,idy)
            adjacent = [line[max(idx-1,0):min(idx+2,len(line))] for line in lines[max(idy-1,0):min(idy+2,len(lines))]]
            counter = [x for x in ".".join(adjacent).replace("*",".").split(".") if x != ""]
            #print(counter)
            count = len(counter)
            return count == 2
        
        def getRatio(gearLoc):
            idx, idy = gearLoc
            a = 0
            b = 0
            #print("\n")
            ratio = -1
            for l in [line[max(idx-3,0):min(idx+4,len(line))] for line in lines[max(idy-1,0):min(idy+2,len(lines))]]:
                for num in [n for n in l.replace("*",".").strip('.').split('.') if n != "" and n not in symbols]:
                    if l.find(num) != -1:
                        if l.find(num) + len(num) >= 3  and l.find(num) <= 4:
                            l.find(num)
                            if ratio == -1:
                                #print("found",num)
                                ratio = int(num)
                                a = int(num)
                            else:
                                ratio *= int(num)
                                #print("found",num,"return")
                                b = int(num)
                                pairs.append((a,b))
                                return ratio
            return "oh fuck"

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

        gearLocs = []
        for idy,line in enumerate(lines):
            idx = 0
            while idx < len(line):
                idx = line.find("*",idx)
                #print(idx,idy)
                if idx == -1:
                    #print("breaking")
                    break
                if isGear((idx,idy)):
                    #print("Gear at",(idx,idy))
                    gearLocs.append((idx,idy))
                else:
                    s = list(line)
                    s[idx] = "."
                    line = "".join(s)
                idx += 1
        for gearLoc in gearLocs:
            part2 += getRatio(gearLoc)
        #print(gearLocs)
        #print(pairs)
        print(part2)