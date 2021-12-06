from functions import *

if __name__ == "__main__":
    i = []
    for x in load('input2.txt'):
        y,z = x.rstrip().split()
        z = int(z)
        i.append((y,z))

    # PART 1
    depth = 0
    pos = 0
    for dir,length in i:
        if dir == 'forward':
            pos += length
        elif dir == 'up':
            depth -= length
        elif dir == 'down':
            depth += length
        else:
            print ("That's a problem.")
        
    print ("PART 1:", depth * pos)

    # PART 2
    depth = 0
    pos = 0
    aim = 0
    for dir,len in i:
        if dir == 'forward':
            pos += len
            depth += aim*len
        elif dir == 'up':
            aim -= len
        elif dir == 'down':
            aim += len
        else:
            print ("That's a problem.")
        #print ("Pos:", pos, ", Depth:", depth, ", Aim:", aim)

    print ("PART 2:", pos*depth)