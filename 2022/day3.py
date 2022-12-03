#https://adventofcode.com/2022/day/3

import sys

def getPriority(item):
    prio = 0
    if ord(item) <= 90:
        prio = ord(item) - 38
    elif ord(item) >= 97:
        prio = ord(item) - 96
    else:
        print("Error in priority get. Quitting.")
        quit()
    return prio

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        #PART 1
        sum = 0
        sacks = []
        for line in file:
            sacks.append(line) #prepping for part 2
            mid = int(len(line.strip())/2)
            item = ""
            for char in line[:mid]:
                if line[mid:].find(char) > -1:
                    item = char
                    break
            sum += getPriority(item)
        print ("Part 1:",sum)

        #PART 2
        sum = 0
        i = 0
        while (i < len(sacks)):
            for char in sacks[i]:
                if sacks[i+1].find(char) > -1 and sacks[i+2].find(char) > -1:
                    item = char
                    break
            sum += getPriority(item)
            i += 3
        print("Part 2:",sum)