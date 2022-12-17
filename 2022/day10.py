#https://adventofcode.com/2022/day/10

import sys
import math

if __name__ == "__main__":

    charges = {20:-1,60:-1,100:-1,140:-1,180:-1,220:-1}
    screen = []

    def checkCycle(cycle):
        if cycle in charges.keys():
            print (cycle,":",x)
            charges.update({cycle:x*cycle})
            
        if abs((x+1) - cycle%40) <= 1:
            screen.append ("#")
        else:
            screen.append (".")
    
    with open(sys.argv[1]) as file:
        cycle = 0
        buffer = 0
        x = 1
        for line in file:
            l = line.strip()
            cycle += 1
            checkCycle(cycle)
            if l == "noop":
                pass
            elif l.startswith("addx"):
                buffer = int(l.split(" ")[1])
                cycle += 1
                checkCycle(cycle)
                x += buffer
        print(charges)
        print(sum(charges.values()))

        #print screen
        for i in range(6):
            print ("".join(screen[i*40:i*40+40]))
        print(len(screen))