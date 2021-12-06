from file_in import load
from datetime import datetime

PREAMBLE_LENGTH = 25

def processInput(l):
    l = load(l)

    numbers = []
    for n in l:
        numbers.append(int(n.strip("\n")))
    return numbers

def isValidNumber (num,previousNums):
    print ("checking if " + str(num) + " is a valid number... ", end='')
    for x in range(len(previousNums)):
        for y in range(x,len(previousNums)):
            #print ("Checking x: " + str(x) + ", " + str(previousNums[x]) + " plus y: " + str(y) + ", " + str(previousNums[y]))
            if previousNums[x] + previousNums[y] == num:
                print ("YEP!")
                return True
    print ("NOPE!")
    return False

def findInvalidNumber (nums):
    print ("--- STARTING TO FIND AN INVALID NUMBER IN INPUT ---\n")
    for line in enumerate(nums):
        if line[0] < PREAMBLE_LENGTH:
            pass
        else:
            if not isValidNumber (line[1], nums[line[0]-PREAMBLE_LENGTH:line[0]]):
                print ("INVALID NUMBER FOUND: " + str(line[1]))
                invalidNumber = line[1]
                break
    return invalidNumber

def findSetForNumber (number, numbers):

    print ("\n--- STARTING TO FIND SET FOR THE INVALID NUMBER: " + str(number) + " ---")
    startIndex = 0

    while startIndex < len(numbers):
        relativeIndex = 0
        currentTotal = 0
        currentRange = []
        while currentTotal <= number:
            currentTotal += numbers[relativeIndex + startIndex]
            currentRange.append (numbers[relativeIndex + startIndex])
            relativeIndex += 1
            if currentTotal == number:
                print ("Found a range: ", end='')
                print (str(currentRange) + ", ", end='')
                print ("this range's encryption weakness is: " + str(min(currentRange) + max(currentRange)))
                break
        startIndex += 1


if __name__ == "__main__":

    nums = processInput("input9.txt")

    invalidNumber = findInvalidNumber (nums)

    findSetForNumber (invalidNumber,nums)