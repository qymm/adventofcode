from file_in import load, checkHex

ROWS_ON_PLANE = 128
COLUMNS_ON_PLANE = 8

def get_input(l):
    l = load(l)

    seats = []
    for n in enumerate(l):
        seats.append (n[1].strip("\n"))
    return seats

def truncateLeft (range):
    return range[:int(len(range)/2)]

def truncateRight (range):
    return range[int(len(range)/2):]

def seatRowColumn (seatCode):
    
    # finding row
    rowRange = [ x for x in range(ROWS_ON_PLANE)]
    for char in seatCode[0:7]:
        if char == 'F':
            rowRange = truncateLeft(rowRange)
        elif char == 'B':
            rowRange = truncateRight(rowRange)
    assert len(rowRange) == 1, "Didn't find single row."
    foundRow = rowRange[0]

    # finding column
    colRange = [ x for x in range(COLUMNS_ON_PLANE)]
    for char in seatCode[7:10]:
        if char == 'L':
            colRange = truncateLeft(colRange)
        elif char == 'R':
            colRange = truncateRight(colRange)
    assert len(colRange) == 1, "Didn't find single column."
    foundColumn = colRange[0]

    return (foundRow, foundColumn)


if __name__ == "__main__":

    i = get_input("input5.txt")

    # converting FB-LR coordinates to row, column
    seatRowCols = [ seatRowColumn(x) for x in i ]

    # seat ID = row times 8 plus column
    seatIDs = [ x*8 + y for (x, y) in seatRowCols ]

    # wanted to make a dictionary
    seatDict = {}
    for x in range(len(seatRowCols)):
        seatDict[i[x]] = {"rowColumn" : seatRowCols[x], "seatID" : seatIDs[x]}
#    for entry in seatDict:
        #print (entry + ": " + str(seatDict[entry]))

    seatIDs.sort()

    # eliminating 
    firstSeat = seatIDs[0]
    lastSeat = seatIDs[len(seatIDs)-1]
    print ("First Seat: " + str(firstSeat))
    print ("Last Seat: " + str(lastSeat))
    
    lastSeat = firstSeat
    for n in seatIDs[1:]:
        if n != lastSeat + 1:
            print ("Found Missing Sequential Seat: " + str(lastSeat+1))
        lastSeat = n
