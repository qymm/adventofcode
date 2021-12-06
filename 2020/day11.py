from file_in import load
import math

STATIC_OCCUPIED = '#'
STATIC_EMPTY = 'L'
STATIC_FLOOR = '.'

def processInput(l):
    l = load(l)

    rows = []
    for n in l:
        rows.append(n.strip("\n"))
    return rows

def checkAdjacentSeats(temp, x,y):

    i = 0

    if x != 0:
        #left
        if temp[y][x-1] == STATIC_OCCUPIED: i += 1
        if y != 0:
            #upper-left
            if temp[y-1][x-1] == STATIC_OCCUPIED: i += 1
        if y < len(temp) - 1:
            #lower-left
            if temp[y+1][x-1] == STATIC_OCCUPIED: i += 1
    if y != 0:
        #up
        if temp[y-1][x] == STATIC_OCCUPIED: i += 1
        if x < len(temp[0]) - 1:
            #upper-right
            if temp[y-1][x+1] == STATIC_OCCUPIED: i += 1
    if y < len(temp) - 1:
        #down
        if temp[y+1][x] == STATIC_OCCUPIED: i += 1
        if x < len(temp[0]) - 1:
            #lower-right
            if temp[y+1][x+1] == STATIC_OCCUPIED:i += 1
    if x < len(temp[0]) - 1:
        if temp[y][x+1] == STATIC_OCCUPIED: i += 1

    return i

def checkLineOfSightSeats(temp, x, y):
    count = 0
    
    #left
    if navLineOfSight(temp,x,y,-1,0): count += 1
    #upper-left
    if navLineOfSight(temp,x,y,-1,-1): count += 1
    #up
    if navLineOfSight(temp,x,y,0,-1): count += 1
    #upper-right
    if navLineOfSight(temp,x,y,1,-1): count += 1
    #right
    if navLineOfSight(temp,x,y,1,0): count += 1
    #lower-right
    if navLineOfSight(temp,x,y,1,1): count += 1
    #down
    if navLineOfSight(temp,x,y,0,1): count += 1
    #lower-left
    if navLineOfSight(temp,x,y,-1,1): count += 1
    
    return count

def navLineOfSight (temp, x, y, xMove, yMove):
    i = 0
    while True:
        i += 1
        if y+(i*yMove) < 0 or x+(i*xMove) < 0 or y+(i*yMove) >= len(temp) or x+(i*xMove) >= len(temp[0]):
            break
        if temp[y+(i*yMove)][x+(i*xMove)] == '#':
            return True
        elif temp[y+(i*yMove)][x+(i*xMove)] == 'L':
            break
    return False


def iterate(rows):

    newRows = []

    for y, row in enumerate(rows):
        newRow = ""
        for x, char in enumerate(row):
            if char == '.':
                newRow += '.'
            elif char == 'L':
                if checkAdjacentSeats(rows,x,y) == 0:
                    newRow += '#'
                else: newRow += 'L'
            elif char == '#':
                if checkAdjacentSeats(rows,x,y) >= 4:
                    newRow += 'L'
                else: newRow += '#'
            else: assert True, "Weird character found."
        newRows.append(newRow)
    nicePrint (newRows)
    return newRows

def iterate2(rows):
    newRows = []
    for y, row in enumerate(rows):
        newRow = ""
        for x, char in enumerate(row):
            if char == '.':
                newRow += '.'
            elif char == 'L':
                if checkLineOfSightSeats(rows,x,y) == 0:
                    newRow += '#'
                else: newRow += 'L'
            elif char == '#':
                if checkLineOfSightSeats(rows,x,y) >= 5:
                    newRow += 'L'
                else: newRow += '#'
            else: assert True, "Weird character found."
        newRows.append(newRow)
    nicePrint (newRows)
    return newRows

def countChars (rows, char):
    count = 0
    for row in rows:
        for i in row:
            if i  == char:
                    count += 1
    return count
                
def nicePrint (rows):
    for row in rows:
        print (row)   
    print ("\n")         

if __name__ == "__main__":

    rows = processInput("input11.txt")

    nicePrint (rows)

    #print( checkLineOfSightSeats(rows,0,0))

    tempRows = []
    while True:
        tempRows = iterate2(rows)
        if tempRows == rows:
            print ("Done")
            print ("Count of occupied chairs: " + str(countChars(tempRows,"#")))
            break
        else:
            rows = tempRows