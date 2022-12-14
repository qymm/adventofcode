#https://adventofcode.com/2022/day/7

import sys

if __name__ == "__main__":

    with open(sys.argv[1]) as file:

        def getSize(dir,arr): #Find size of every directory contained within dir
            size = 0
            for x in dir:
                if isinstance(dir[x],dict):
                    size += getSize(dir[x],arr)
                elif isinstance(dir[x],int):
                    size += dir[x]
            arr.append(size) #Processed a new directory.
            return size

        def parseDirectory(dir): #Traverse input to create nested dicts
            currentDir = dir
            tree = {}
            while file:
                line = file.readline()
                if line.startswith("$ cd .."):
                    print("traversing back")
                    return tree
                elif line == "":
                    print("EOF")
                    return tree
                elif line.startswith("$ cd"):
                    currentDir = line.strip().split(" ")[-1]
                    print("changing directory to", currentDir)
                elif line.startswith("$ ls"):
                    print("recursing to", currentDir)
                    tree.update({currentDir:parseDirectory(currentDir)})
                else:
                    x, name = line.strip().split(" ")
                    if x == "dir":
                        print("found dir",name)
                        tree.update({name:{}})
                    else:
                        print("found file",name,x)
                        tree.update({name:int(x)})
        
        dirs = []

        root = parseDirectory("/")
        rootSize = getSize (root, dirs)  

        print(sum([x for x in dirs if x <= 100000])) #P1

        needToDelete = rootSize - 40000000
        dirs.sort()
        for x in dirs:
            if x > needToDelete:
                print (x) #P2
                break