

def loadFile(s):
    with open(s) as file:
        i = []
        j = []
        for idx,line in enumerate(file.readlines()):
            i.append (line.split("|")[0].strip())
            j.append (line.split("|")[1].strip())
    return i,j

#7 chars means 8
#6 chars means 0, 6, or 9
#5 chars means 2, 3, or 5
#4 chars means 4
#3 chars means 7
#2 chars means 1

def mapNumbers(pattern):
    items = pattern.split()
    values = {0:"",1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}

    for x in items:
        if len(x) == 2:
            values[1] = x
        elif len(x) == 3:
            values[7] = x
        elif len(x) == 4:
            values[4] = x
        elif len(x) == 7:
            values[8] = x

    #chars that are in 4, but not in 1
    topLeftAndMid = "".join([i for i in values[4] if i not in values[1]])

    for x in items:
        if len(x) == 5:
            #5 lights, including those in '1' means '3'
            if values[1][0] in x and values[1][1] in x:
                values[3] = x
            #5 lights, including those that differentiate '4' and '1', means '5'
            elif topLeftAndMid[0] in x and topLeftAndMid[1] in x:
                values[5] = x
            #5 lights, but neither of the above, means '2'
            else:
                values[2] = x
        elif len(x) == 6:
            #6 lights, without including both the difference between '4' and '1', means '0'
            if not ((topLeftAndMid[0] in x) and (topLeftAndMid[1] in x)): 
                values[0] = x
            #6 lights, including those in '1', means '9'
            elif values[1][0] in x and values[1][1] in x:
                    values[9] = x
            #6 lights, but not the ones above, means '6'
            else:
                values[6] = x

    #print (values)
    if len(values.keys()) != 10:
        print ("ERROR: Length incorrect.")
    else:
        return values

def findElemInDict(elem,keyDict):
    for key,value in keyDict.items():
        if 0 not in [c in elem for c in value] and len(value) == len(elem):
            #print ("Elem found:", key)
            return key

if __name__ == "__main__":
    i,j = loadFile("input8.txt")
        
    def solvePart1(j):
        count = 0
        for row in j:
            for number in row.split():
                if len(number) == 7 or len(number) == 4 or len(number) == 3 or len(number) == 2:
                    count += 1
        return count

    def solvePart2(i,j):
        outputSum = 0
        for idx,line in enumerate(j):
            tempNum = []
            key = mapNumbers(i[idx])
            for elem in line.split():
                tempNum.append(findElemInDict(elem,key))
            tempNum = "".join([str(x) for x in tempNum])
            outputSum += int(tempNum)
        return outputSum

    print ("PART 1:",solvePart1(j))

    print ("PART 2:",solvePart2(i,j))