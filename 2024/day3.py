#https://adventofcode.com/2024/day/3

import sys
import string

if __name__ == "__main__":

    def isATuple(s): # chatgpt reminded me what the hell the syntax for this is
        try: 
            result = eval(s)
            if isinstance(result,tuple):
                return True,result
            else:
                return False,(-1,-1)
        except (SyntaxError, NameError):
            return False,(-1,-1)

    with open(sys.argv[1]) as file:
        lines = [l.rstrip() for l in file]
        line = "".join(lines) # fuck line breaks
        found = True
        part1 = 0
        while found: # simple loop for simple monkey brain
            i = line.find("mul(") # find the beginning and end of this mul(...)
            i2 = line[i:].find(")")
            if i == -1: # if cannot find "mul(", we are done
                found = False
            result = isATuple(line[i+3:i+i2+1]) # is the contents of mul(...) a tuple?
            print(isATuple(line[i+3:i+i2+1]))
            if result[0]:
                part1 += result[1][0] * result[1][1] # if so, add the tuple's product
            line = line[i+3:] # move along
        print (part1)

        line = "".join(lines) # all my homies hate line breaks
        enabled = True
        part2 = 0
        while True:
            iMul = line.find("mul(") # find earliest index of each function
            iMul2 = line[iMul:].find(")")
            iDo = line.find("do()")
            iDont = line.find("don't()")
            # picks action based on lowest index, not including if index is -1
            if iMul != -1 and (iMul < iDo or iDo == -1) and (iMul < iDont or iDont == -1):
                result = isATuple(line[iMul+3:iMul+iMul2+1])
                print(isATuple(line[iMul+3:iMul+iMul2+1]))
                if result[0] and enabled:
                    part2 += result[1][0] * result[1][1]
                line = line[iMul+3:]
            elif iDo != -1 and (iDo < iMul or iMul == -1) and (iDo < iDont or iDont == -1):
                print ("Enabling")
                enabled = True
                line = line[iDo+2:]
            elif iDont != -1 and (iDont < iMul or iMul == -1) and (iDont < iDo or iDo == -1):
                print ("Disabling")
                enabled = False
                line = line[iDont+5:]
            else:
                print(iMul,iDo,iDont,"Ding!") # we are done!
                break
        print(part2)
