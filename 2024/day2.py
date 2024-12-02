#https://adventofcode.com/2024/day/2

import sys
import string

if __name__ == "__main__":

    def safe(rep):
        r = [int(x) for x in rep.split()]
        sign=r[1]-r[0] #saving directionality to check against
        for i in range(1,len(r)):
            if abs(r[i]-r[i-1]) > 3 or (r[i]-r[i-1])*sign < 0 or r[i]==r[i-1]: #if unsafe for any reason
                return False
        return True
    
    def safe2(rep,canPop):
        r = [int(x) for x in rep.split()]
        #print (r)
        sign=r[1]-r[0]
        for i in range(1,len(r)):
            if abs(r[i]-r[i-1]) > 3 or (r[i]-r[i-1])*sign < 0 or r[i]==r[i-1]: #if unsafe for any reason
                if canPop:
                    for j in range(len(r)): #pop each index and check if any variation is safe
                        temp = list(r)
                        temp.pop(j)
                        temp = " ".join(map(str, temp)) #safe2 wants a str
                        if (safe2(temp,False)): #canPop = False here means it won't attempt to recurse again
                            #print(temp, "Safe")
                            return True
                    #print(temp, "Unsafe")
                    return False
                else:
                    return False
        #print(r, "Safe")
        return True

    with open(sys.argv[1]) as file:
        reports = [l.rstrip() for l in file]
        print ("p1:", len([r for r in reports if safe(r)]))
        print ("p2:", len([r for r in reports if safe2(r,True)]))