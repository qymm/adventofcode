#https://adventofcode.com/2023/day/2

import sys
import string

if __name__ == "__main__":
    
    with open(sys.argv[1]) as file:
        lines = [l.rstrip() for l in file]
        games = []

        def returnRGB(game): #the minimum RGB values needed for a given game
            rgb = [0,0,0]
            counts = game.replace(';',',').split(',')
            for count in counts:
                x = (int)(count.split()[0])
                if count.endswith('red') and rgb[0] < x:
                    rgb[0] = x
                elif count.endswith('green') and rgb[1] < x:
                    rgb[1] = x
                elif count.endswith('blue') and rgb[2] < x:
                    rgb[2] = x
            return rgb

        for l in lines:
            rgbs = []
            l = l.split(':')[1].strip() #remove header
            games.append(returnRGB(l))

        def validRGB(xyz): #is this a possible game in part 1?
            return (xyz[0] <= 12) and (xyz[1] <= 13) and (xyz[2] <= 14)

        part1 = 0
        for i,game in enumerate(games):
            if validRGB(game):
                part1 = part1 + (i + 1)
        print(part1)

        part2 = 0
        for xyz in games:
            part2 = part2 + xyz[0]*xyz[1]*xyz[2] #the power of a game in part 2
        print(part2)