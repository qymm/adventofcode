def process_input_ints(l):
    o = []
    with open(l) as f:
        l = f.readlines()
    for n in l:
        o.append(int(n))
    return o

if __name__ == "__main__":
    i = process_input_ints('day1-input.txt')

    ### PART 1
    #print (i)

    #prev = 999999999999999
    #count = 0
    #for x in i:
    #    if prev < x:
    #        count += 1
    #        print (x)
    #    prev = x

    #print (count)

    ### PART 2
    count = 0

    j = []
    for x in range(len(i)-2):
        j.append(i[x]+i[x+1]+i[x+2])
    
    print (j)

    prev = 999999999999
    for x in j:
        if prev < x:
            count += 1
            #print (x)
        prev = x

    print (count)