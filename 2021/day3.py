from functions import *

if __name__ == "__main__":

    file = 'input3.txt'
    staticLength = len(open(file).readline().strip())


    #Counts the "1"s in each column and returns gamma and epsilon.
    def getGammaEpsilonBinary (arr):
        def createCountArrays (arr):
            zerosArr = [0] * staticLength
            onesArr = [0] * staticLength
            for x in arr:
                for digit in range(staticLength):
                    if int(x[digit]) == 1:
                        onesArr[digit] += 1
            zerosArr = [ len(arr) - one for one in onesArr ]
            return zerosArr,onesArr

        zeros,ones = createCountArrays(arr)

        def getGreaterBit (one,zero):
            if one == zero:
                return "#"
            elif one > zero:
                return "1"
            else:
                return "0"

        #print ("Ones:", ones)
        #print ("Zeros:",zeros)
        gamma = (''.join(map(getGreaterBit,ones,zeros)))
        epsilon = (''.join(map(getGreaterBit,zeros,ones)))
        return gamma, epsilon

    ### PART 1
    gamma, epsilon = getGammaEpsilonBinary(load(file))
    # Print BINtoDEC converstion.
    print ("Gamma:",int(gamma,2))
    print ("Epsilon:",int(epsilon,2))
    print ("PART 1:",int(gamma,2)*int(epsilon,2))

    ### PART 2
    # Start both oxy and co2 at full list.
    oxy = [ z.strip() for z in load(file) ]
    co2 = [ z for z in oxy ]

    # Given an array of strings, finds the gamma/mode digit value of a specified column/digit.
    # "#" string specifies that a "1" is given, because of how we end up using this function to check against oxy vs. co2.
    def getModeAtBit(arr,bit):
        gam,ep = getGammaEpsilonBinary(arr)
        if gam[bit] == "#":
            return "1"
        else:
            return gam[bit]

    # Loops digits to find oxy.
    for digit in range(staticLength):
        j = 0
        # Checks for new gamma bit every new column.
        curGammaBit = getModeAtBit(oxy,digit)
        while j < len(oxy):
            if len(oxy) == 1:
                # Stop if having reached last element in array.
                break
            elif (oxy[j][digit] != curGammaBit):
                #print ("Popping OXY:", oxy[j])
                oxy.pop(j)
            else:
                # Move on if no pop occurred.
                j += 1
    # Loops digits to find co2.
        k = 0
        # Checks for new gamma bit every new column.
        curGammaBit = getModeAtBit(co2,digit)
        while k < len(co2):
            if len(co2) == 1:
                # Stop if having reached last element in array.
                break
            elif (co2[k][digit] == curGammaBit):
                #print ("Popping CO2:", co2[k])
                co2.pop(k)
            else:
                # Move on if no pop occurred.
                k += 1

    # BINtoDEC conversion.
    oxy = int(oxy[0],2)
    co2 = int(co2[0],2)
    print("OXY:",oxy)
    print("CO2:",co2)
    print("PART 2:",oxy*co2)