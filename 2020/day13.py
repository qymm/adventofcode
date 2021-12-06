from file_in import load
import math

def processInput(l):
    l = load(l)

    buses = []
    allBuses =[]
    for n in enumerate(l):
        if n[0] == 0:
            startTime = int(n[1])
        else:
            temp = n[1].strip("\n").split(',')
            for x in temp:
                if not x == "x":
                    buses.append(int(x))
                    allBuses.append(int(x))
                else:
                    allBuses.append(-1)
    return startTime, buses, allBuses

def findNextBus(currentTime, buses):
    for bus in buses:
        if currentTime % bus == 0:
            return bus
    return -1

def findConsecutiveBuses(t, allBuses):
    for step,bus in reversed(list(enumerate(allBuses))):
        if bus == -1:
            pass
        elif (t+step) % bus != 0:
            return False
    return True

def solve_crt(minusList, busList):
    bigMultiple = 1
    for bus in busList:
        bigMultiple *= bus
    Mi = [bigMultiple // busList[i] for i in range(len(busList))]
    yi = [inverse(Mi[i], busList[i]) for i in range(len(busList))]
    X = sum([minusList[i] * Mi[i] * yi[i] for i in range(len(yi))])
    return (X%bigMultiple)

def inverse (start,mod):
    t = 0
    newt = 1
    r = mod
    newr = start

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)
    
    if r > 1:
        raise Exception("start value not invertible")
    if t < 0:
        t += mod
    
    return t

if __name__ == "__main__":
    i = processInput("input13.txt")
    startTime = i[0]
    buses = i[1]
    allBuses = i[2]
    print (i)


    #solution 1
    currentTime = startTime
    while True:
        tempBus = findNextBus(currentTime,buses)
        if not tempBus == -1:
            print ("Found: " + str(tempBus))
            break
        else:
            currentTime += 1
    print ("Solution 1: " + str((currentTime - startTime)*tempBus))

    #solution 2
    minusedList = [int(v) - idx for idx, v in enumerate(allBuses) if not v == -1]
    print("minused list: " + str(minusedList))
    busList = [int(v) for v in allBuses if not v == -1]
    print("bus list: " + str(busList))
    sol = solve_crt(minusedList,busList)
    print ("Solution 2: " + str(sol))