from functions import *
import statistics

def loadCrab(s):
    #list method
    with open(s) as file:
        i = [int(x) for x in file.read().split(",")]
    return i

if __name__ == "__main__":
    ishtars = loadCrab("input7.txt")

    #PART 1 - AKA QYMM FIGURED IT OUT
    print (int(statistics.median(ishtars)))
    fuelCost = int(sum([ abs(x - statistics.median(ishtars)) for x in ishtars ]))
    print (fuelCost)
    
    #PART 2 - AKA QYMM CAN'T RECOGNIZE MATH PROBLEMS
    ishtars.sort()
    fuelCosts = []
    for i in range(ishtars[0], ishtars[-1] + 1):
        fuelCosts.append (sum([ abs(i - x) * (abs(i - x) + 1) / 2 for x in ishtars ]))
    fuelCosts.sort()
    print (fuelCosts[0])