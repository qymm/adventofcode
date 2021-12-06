from file_in import load
from file_in import nicePrint
import math

MASK_LENGTH = 36
mask = ''.join([ "0" for x in range(MASK_LENGTH) ])

def processInput(l):
    l = load(l)

    lines = []
    for n in l:
        lines.append (n.strip("\n"))
    return lines

def setNewMask(input):
    global mask
    m = input.rsplit(" ", 1)
    mask = m[1]
    print ("New mask:", m[1])

def convertToBinary(input):
    result = '{0:036b}'.format(input)
    return result

def convertToDec(input):
    binary = int(input.lstrip("0"))
    decimal, i, n = 0,0,0
    while (binary != 0):
        dec = binary % 10
        decimal += dec * pow (2,i)
        binary = binary//10
        i += 1
    return (decimal)

def maskThis(input):
    global mask
    temp = ""
    for i in range(MASK_LENGTH):
        if mask[i] == "X":
            temp = ''.join((temp,input[i]))
        else:
            temp = ''.join((temp,mask[i]))
    return temp

if __name__ == "__main__":
    f = processInput("input14.txt")

    mem = {}

    for line in f:
        if line.find("mask") != -1:
            setNewMask(line)
        elif line.find("mem") != -1:
            i = line.rsplit(" ",1)

            #get the mem index
            x = i[0]
            x = int(x.split("[",1)[1].strip("] = "))

            #the input
            i = int(i[1])
            i = convertToBinary(i)
            mem[x] = maskThis(i)

    #find total
    sum = 0
    for key in mem.keys():
        
        sum += convertToDec(mem.get(key))

    print ("Solution 1: ", sum)
            
    mem = {}
    for line in f:
        if line.find("mask") != -1:
            setNewMask(line)
            line(
        elif line.find("mem") != -1:
            i = line.rsplit(" ",1)

            #get the mem index
            x = i[0]
            x = x.split("[",1)[1].strip("] = ")

            #get what to write
            i = int(i[1])
            #i = convertToBinary(i)

            a = [convertToBinary(int(x))]
            #nicePrint([mask])
            #print(convertToBinary(int(x)))
            #print("----------")
            for j in range(MASK_LENGTH):
                if mask[j] == "X":
                    nA = []   
                    for address in a:
                        nA.append (address[0:j] + "0" + address[j+1: ])
                        nA.append (address[0:j] + "1" + address[j+1: ])
                    a = nA
                elif mask[j] == "1":
                    nA = []
                    for address in a:
                        nA.append (address[0:j] + "1" + address[j+1: ])
                    a = nA
            #nicePrint (a)

            print ("Writing", '{0:<10}'.format(i) ,"to", '{0:<3}'.format(len(a)), "addresses.")
            for address in a:
                #print (i)
                mem[convertToDec(address)] = i

    sum = 0
    for key in mem.keys():
        #sum += convertToDec(mem.get(key))
        sum += mem.get(key)

    print ("Solution 2: ", sum)        