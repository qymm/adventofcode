from file_in import load
import math

def processInput(l):
    l = load(l)

    numbers = []
    for n in l:
        numbers.append(int(n.strip("\n")))
    return numbers

def findDifferences(nums):

    # adding the joltage port
    nums.append(0)
    # adding the joltage adapter of your device
    nums.append(max(nums)+3)

    #print (nums)
    nums.sort()

    differences = {}
    for x in range(len(nums)-1):
        debug = nums[x]
        debug2 = nums[x+1]
        difference = nums[x+1] - nums[x]
        if differences.get(difference) == None:
            differences.update({difference:0})
        differences[difference] += 1
        
    return differences

def iterate(sorted, index):
    tempCount = 0
    if sorted[index] == max(sorted):
        tempCount += 1
        return tempCount
    try:
        if sorted[index+3] <= sorted[index] + 3:
            tempCount += iterate(sorted, index+3)
    except IndexError: pass        
    try:
        if sorted[index+2] <= sorted[index] + 3:
            tempCount += iterate(sorted, index+2)
    except IndexError: pass
    try:
        if sorted[index+1] <= sorted[index] + 3:
            tempCount += iterate(sorted, index+1)
    except IndexError: pass
    return tempCount

def findValidLengths(nums):

    global validCount
    validCount = 0


    # didn't work, ask Fwosty
    # nums.sort(reverse=True)

    # def waysToMax (nums,index):
    #     tempCount = 0
    #     try:
    #         if index >= 1 and nums[index-1] <= nums[index] + 3:
    #             tempCount += ways.get(nums[index-1])
    #     except IndexError: pass
    #     try:
    #         if index >= 2 and nums[index-2] <= nums[index] + 3:
    #             tempCount += ways.get(nums[index-2])
    #     except IndexError: pass
    #     try:
    #         if index >= 3 and nums[index-3] < nums[index] + 3:
    #             tempCount += ways.get(nums[index-3])
    #     except IndexError: pass
    #     return tempCount

    # ways = {173: 1}
    # for x in range(1,len(nums)):
    #     temp = waysToMax(nums, x)
    #     ways.update({nums[x]:temp})

    # return ways

    nums.sort()
    lists = []
    lastKnown = 0
    for x in range(len(nums)):
        try:
            if nums[x+1] == nums[x] + 3:
                tempList = [ y for y in nums[lastKnown:x+1] ]
                lists.append ( tempList )
                lastKnown = x + 1
        except IndexError: pass
    lists.append([173])

    paths = []
    print (lists)
    for x in lists:
        paths.append(iterate(x, 0))
    print (paths)

    def multiplyList(theList):
        result = 1
        for x in theList:
            result = result * x
        return result

    return multiplyList(paths)


if __name__ == "__main__":

    i = processInput("input10.txt")
    
    diffs = findDifferences(i)
    print ("Differences: " + str(diffs))

    print ("Part 1 answer: " + str(diffs.get(1) * diffs.get(3)))
    i = processInput("input10.txt")
    # adding the joltage port
    i.append(0)
    # adding the joltage adapter of your device
    i.append(max(i)+3)
    validLengths = findValidLengths (i)
    print (validLengths)