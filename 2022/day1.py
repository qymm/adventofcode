#https://adventofcode.com/2022/day/1

import sys

# because I didn't know that I could just sort()
def insertElf(l,count):
    for i in range(len(l)):
        if count >= l[i]:
            l.insert(i,count)
            #print ("inserted")
            return
    l.append (count)
            
if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        #shortened this parse, because I always forget Python can be so compact
        lines = [l.rstrip() for l in file]

        print(lines)
        elves = []
        subtotal = 0
        for line in lines:
            if not line:
                insertElf(elves,subtotal)
                subtotal = 0
            else:
                subtotal += int(line)
        if subtotal > 0:
            insertElf(elves,subtotal)
        #almost forgot the last elf
        print ("Part 1:",elves[0])
        #tried to find a sum function initially, but ended up getting impatient and just adding by hand
        print ("Part 2:",sum(elves[:3]))