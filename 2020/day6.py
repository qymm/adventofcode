from file_in import load
import string

def get_input(l):
    l = load(l)

    flatAnswers = []
    
    flatGroup = ""
    for n in enumerate(l):
        if n[1]  != "\n":
            flatGroup += n[1].strip()
        if n[1] == "\n" or n[0] == len(l) - 1:
            res = []
            [res.append(x) for x in flatGroup if x not in res]
            #res = flatGroup
            res.sort()
            flatAnswers.append(res)
            flatGroup = ""

    return flatAnswers

def get_input2(l):
    l = load(l)
    flatAnswersWithDupes = []

    flatGroup = ""
    groupMembers = []
    numPeople = 0
    for n in enumerate(l):
        if n[1]  != "\n":
            flatGroup += n[1].strip()
            numPeople += 1
        if n[1] == "\n" or n[0] == len(l) - 1:
            flatAnswersWithDupes.append(flatGroup)
            groupMembers.append(numPeople)
            flatGroup = ""
            numPeople = 0

    return (flatAnswersWithDupes, groupMembers)

if __name__ == "__main__":

    i = get_input("input6.txt")

    # summing counts
    sum = [ len(x) for x in i ]
    #print(sum)
    sumSum = 0
    for x in sum:
        sumSum += x

    print (sumSum)

    i,j = get_input2("input6.txt")

    sumEveryones = []
    for n,v in enumerate(i):
        sumThisGroup = 0
        for c in string.ascii_lowercase:
            count = v.count(c)
            if count == j[n]:
                sumThisGroup += 1
        sumEveryones.append(sumThisGroup)
    
    print(sumEveryones)
    sumSum = 0
    for x in sumEveryones:
        sumSum += x
    print(sumSum)