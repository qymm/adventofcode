#https://adventofcode.com/2022/day/4

import sys

def asRange(i):
    j = i.split("-")
    return (list(range(int(j[0]),int(j[1])+1)))

if __name__ == "__main__":
    pairs = []

    with open(sys.argv[1]) as file:
        for line in file:
            pairs.append (line.strip().split(","))
        print (pairs)

    p1count = 0
    for pair in pairs:
        i = asRange(pair[1])
        j = asRange(pair[0])
        if len(asRange(pair[1])) > len(asRange(pair[0])):
            k = j
            j = i
            i = k
        x = j[0] <= i[0]
        print(j[0],"<=",i[0],"=",x)
        y = i[-1] <= j[-1]
        print(i[-1],"<=",j[-1],"=",y)
        z = x ^ y
        print("Is valid list?",z)
        if not z:
            p1count += 1
    print (p1count)

    p2count = 0
    for pair in pairs:
        overlap = [x for x in asRange(pair[1]) if x in asRange(pair[0])]
        if len(overlap) > 0:
            p2count += 1
    print (p2count)