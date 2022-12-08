#https://adventofcode.com/2022/day/5

import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        rows = []

        for line in file:
            if line[1].isnumeric():
                break #end of boxes
            else:
                rows.append ([line[i:i+3].strip() for i in range(0,len(line),4)])

        stacks = [[rows[i][j].strip("[]") for i in range(len(rows)) if rows[i][j] != ''] for j in range(len(rows[0]))]

        for stack in stacks:
            stack.reverse()

        solvePart2 = True

        for line in file:
            if line.strip(): #skip first blank line
                x,y,z = [int(i) for i in line.split() if i.isnumeric()]
                #instr = [int(i) for i in instr if i.isnumeric()]
                #print(instr)
                if solvePart2:
                    stacks[z-1].extend(stacks[y-1][x*-1:])
                    stacks[y-1] = stacks[y-1][:x*-1]
                else:
                    for n in range(x):
                        stacks[z-1].append(stacks[y-1].pop())
        answer = ''.join([stacks[i][-1] for i in range(len(stacks))])

        print(answer)