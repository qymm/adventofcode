from functions import *

def loadFish(s):
    with open(s) as file:
        i = [int(x) for x in file.read().split(",")]
    return i

def loadFishDict(s):
    fishDict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    with open(s) as file:
        i = [int(x) for x in file.read().split(",")]
        for j in i:
            if j in fishDict:
                fishDict.update({j: fishDict[j]+1})
    return fishDict
            
if __name__ == "__main__":
    fishies = loadFish("input6.txt")
    #cooldowns = [c for c in fishies]
    
    #PART1
    def tickFish(fishes):
        newFishies = []
        for idx,fish in enumerate(fishes):
            if fish > 0:
                fishes[idx] -= 1
            elif fish == 0:
                newFishies.append(8)
                fishes[idx] = 6
        return newFishies

    print (fishies)
    for x in range(80):
        newFish = tickFish(fishies)
        fishies = fishies + newFish
        #print (fishies)
    print (len(fishies))

    def tickFishDict(fishies):
        newFishies = fishies[0]
        for x in range(1,9):
            fishies[x-1] = fishies[x]
        fishies[6] = fishies[6] + newFishies
        fishies[8] = newFishies

    fishies = loadFishDict("input6.txt")
    
    print(fishies)
    for x in range(256):
        tickFishDict(fishies)
        print(fishies)
    print(sum([x for x in fishies.values()]))