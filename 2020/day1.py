def process_input(l):
    o = []
    with open(l) as f:
        l = f.readlines()
    for n in l:
        o.append(int(n))
    return o

if __name__ == "__main__":
    i = process_input('input1.txt')

    for x in i:
        for y in i:
            if x + y == 2020:
                print (x*y)
                break

    for x in range(len(i)):
        for y in range(x,len(i)):
            for z in range(y,len(i)):
                if i[x] + i[y] + i[z] == 2020:
                    print ("x: " + str(x) + ", y: " + str(y) + ", z: " + str(z))
