#https://adventofcode.com/2024/day/1

import sys
import string
            
if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        lines = [l.rstrip() for l in file]
        arr1 = sorted(int(l.split()[0]) for l in lines)
        arr2 = sorted(int(l.split()[-1]) for l in lines)
        arr3 = [abs(y-x) for x,y in zip(arr1,arr2)]
        print("p1:",sum(arr3))

        dict1 = {}
        for num in arr1:
            if(arr2.count(num) > 0):
                dict1.update({num: arr2.count(num)})
        arr3 = [key*dict1[key] for key in dict1.keys()]
        print ("p2:",sum(arr3))