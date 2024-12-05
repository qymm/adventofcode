#https://adventofcode.com/2024/day/4

import sys
import string

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        lines = [l.rstrip() for l in file]
        i = lines.index('') # separating the rules from the updates
        rules = lines[:i]
        updates = lines[i+1:]

        ruleDict = {} # creating dict of numbers to succeeding numbers
        for r in rules:
            x,y = list(map(int,r.split('|')))
            if y in ruleDict:
                pass
            else:
                ruleDict[y] = []
            if x in ruleDict:
                temp = ruleDict[x]
                temp.append(y)
                ruleDict[x] = temp
            else:
                ruleDict[x] = [y]

        def createKey(d): # create an ordered key that holds every number, based on the notion that length of succeeding numbers is the inverted position of the number in a list containing all numbers   
            key = [-1] * 999
            for k in d.keys():
                key[len(d[k])] = k
            key = key[::-1]
            key = [x for x in key if x != -1]
            return key

        # ok, that assumption was a bit incorrect. I can't use a monolithic key for Part 2. I must first eliminate entries for numbers that aren't in the update at all, per update; that actually reveals the length of succeeding numbers I need.
        
        def countSolution(updates):
            count = 0
            for u in updates:
                #print(int(len(u)/2))
                count += u[int(len(u)/2)] # get middle page
            return count

        good = []
        bad = []
        for u in updates: # separating good from bad updates
            flag = True
            book = list(map(int,u.split(',')))
            for n in range(len(book)-1,-1,-1):
                if set(ruleDict[book[n]]) & set(book[0:n]): # is breaking rules?
                    flag = False
                    bad.append(book) # add to naughty list
                    break
            if flag:
                good.append(book) # add to nice list

        print ("P1:",countSolution(good))

        fixed = []
        for b in bad: # fixing the bad updates
            tempRules = {}
            for k in ruleDict.keys():
                if k in b:
                    tempRules[k] = [x for x in ruleDict[k] if x in b]
            tempKey = createKey(tempRules)
            fixed.append(tempKey) # the key just turns out to be the entire update after all of that!

        print("P2:",countSolution(fixed))