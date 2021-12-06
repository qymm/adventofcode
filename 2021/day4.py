from functions import *

def parseBingoInput (s):
    draws = [ int(x) for x in open(s).readline().strip().split(',') ]

    i = load(s)
    boards = []
    for j in range(len(i)):
        if i[j] == "\n":
            m = []
            for k in range(j+1,j+6):
                l = [ (int(kk.strip()),0) for kk in i[k].split(" ") if kk != "" ]
                m.append(l)
            boards.append(m)
    return draws,boards

def printBoard (board):
    for i in board:
        print (i)
    print ("")

def markBoard (board,num):
    for row,spots in enumerate(board):
        for spot,value in enumerate(spots):
            if value[0] == num:
                #print ("Found", num, "in spot", spot+1, "in row", row+1, "marking.")
                board[row][spot] = (num,1)
    
def checkForBingo (board):
    #checking horizontal
    for row in board:
        if sum([ y for x,y in row if y == 1]) == 5:
            return 1
    #checking vertical
    for colIdx in range(len(board[0])):
        col = [ x[colIdx] for x in board ]
        if sum([ x[1] for x in col ]) == 5:
            return 1
    return 0

def getScore (board, num):
    boardSum = sum ([ sum ([ spot for spot,mark in row if mark == 0 ]) for row in board ])
    print ("boardSum:", boardSum, "+", "num:", num, "=",boardSum*num)
    return boardSum * num

if __name__ == "__main__":

    draws,boards = parseBingoInput("input4.txt")
    bingoFound = 0
    #Part 1
    for draw in draws:
        for idx,board in enumerate(boards):
            markBoard(board,draw)
            if checkForBingo(board):
                print ("PART1: Board",idx, "has bingo!")
                #printBoard (board)
                bingoFound = 1
                getScore(board,draw)
            if bingoFound: break
        if bingoFound: break

    draws,boards = parseBingoInput("input4.txt")
    bingoFound = 0

    #Part 2
    for draw in draws:
        #print ("Calling number", draw)
        for idx,board in enumerate(boards):
            markBoard(board,draw)
        for idx,board in enumerate(boards):
            if checkForBingo(board):
                print ("PART2: Board",idx, "has bingo!")
                if len(boards) == 1:
                    getScore(board,draw)
                    bingoFound = 1
                else:
                    print ("Popping board:", idx)
                    boards.pop(idx)
            if bingoFound: break
        if bingoFound: break