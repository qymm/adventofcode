#https://adventofcode.com/2022/day/9

import sys
import math

if __name__ == "__main__":

    dir = {
        "R": (1,0),
        "L": (-1,0),
        "U": (0,-1),
        "D": (0,1)
    }

    def follow (head,tail):
        if (abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1):
                pass
        else:
            if abs(head[0]-tail[0]) > 1:
                tail = tail[0]+math.copysign(1,(head[0]-tail[0])),tail[1]
                if head[1] != tail[1]:
                    tail = tail[0],tail[1]+math.copysign(1,(head[1]-tail[1]))
            elif abs(head[1]-tail[1]) > 1:
                tail = tail[0],tail[1]+math.copysign(1,(head[1]-tail[1]))
                if head[0] != tail[0]:
                    tail = tail[0]+math.copysign(1,(head[0]-tail[0])),tail[1]
            else:
                raise Exception ("That's weird.")
        if not (abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1):
            raise Exception("Why aren't these touching?")
        return tail

    with open(sys.argv[1]) as file:
        tailPositions = set()
        tailPositions2 = set()
        head = (0,0)
        tail = (0,0)
        p2rope = [(0,0) for x in range(10)]

        for line in file:
            d, n = line.strip().split()
            for i in range(int(n)):
                head = head[0]+dir[d][0],head[1]+dir[d][1]
                tail = follow(head,tail) #P1
                tailPositions.add (tail)

                p2rope[0] = p2rope[0][0]+dir[d][0],p2rope[0][1]+dir[d][1]

                for i,k in enumerate(p2rope): #P2
                    if i == 0:
                        pass
                    else:
                        p2rope[i] = follow(p2rope[i-1],p2rope[i])
                tailPositions2.add(p2rope[9])

        print ("P1:",len(tailPositions))
        print ("P2:",len(tailPositions2))