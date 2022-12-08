#https://adventofcode.com/2022/day/6

import sys

if __name__ == "__main__":
    def solve (line,length):
        for n,c in enumerate(line):
            s = set([c for c in line[n-length:n]])
            if len(s) >= length:
                return n

    with open(sys.argv[1]) as file:
        for line in file:
            print("P1:",solve(line,4))
            print("P2:",solve(line,14))