#https://adventofcode.com/2023/day/1

import sys
import string
            
if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        #shortened this parse, because I always forget Python can be so compact
        lines = [l.rstrip() for l in file]

        spells = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }

        nums = [] 
        for line in lines:
            y = ""
            x = ""
            for idx,c in enumerate(line):
                if c.isnumeric():
                    x = c
                    break
                else:
                    for key in spells.keys(): #find dict words
                        a = line[idx:idx+len(key)]
                        if (a == key):
                            x = spells[key]
                            break
                    if x != "": break
            for idx,c in enumerate(reversed(line)):
                if c.isnumeric():
                    y = c
                    break
                else:
                    for key in spells.keys(): #find dict words, in reverse
                        b = line[len(line)-idx-len(key):len(line)-idx]
                        #print (b)
                        if (b == key):
                            y = spells[key]
                            break
                    if y != "": break
       
            nums.append((int)(x+y)) #concatenate
        print(sum(nums))