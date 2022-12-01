def load(s):
    o = []
    with open(s) as input:
        l = input.readlines()
        for line in l:
            o.append(line.rstrip())
    return o

def insertElf(l,count):
    for i in range(len(l)):
        if count >= l[i]:
            l.insert(i,count)
            print ("inserted")
            return
    l.append (count)
            
if __name__ == "__main__":
    i = load("input1.txt")
    print(i)
    max = 0
    elves = []
    subtotal = 0
    for line in i:
        if line == '':
            insertElf(elves,subtotal)
            subtotal = 0
        else:
            subtotal += int(line)
    print (elves[0],elves[1],elves[2])
    print (elves[0]+elves[1]+elves[2])