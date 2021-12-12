import sys

def load(s):
    with open(s) as file:
        i = [line.strip() for line in file.readlines()]
    return i

def loadConnections(lines):
    connections = {} 
    for line in lines:
        a,b = line.split("-")
        if a in connections.keys():
            connections[a].append(b)
        else:
            connections[a] = [b]
        if b in connections.keys():
            connections[b].append(a)
        else:
            connections[b] = [a]

    #removing "start" as an ending connection for optimization
    for key in connections.keys():
        if "start" in connections[key]:
            connections[key].remove("start")

    return connections

def findRoutes(connections,part):

    #Check if the working route already has a revisited small cave.
    def hasSmallDuplicates(r):
        s = [ c for c in r if c.islower() and c != "start" ]
        if len(s) > 1 and len(s) != len(set(s)):
            return True
        else:
            return False

    #Adds all valid routes as new possible routes, then removes the originative incomplete route.
    def addConnections(routes,route):
        for idx,connection in enumerate(connections[route[-1]]):
            if part == 1:
                if (connection.islower() and connection != "start" and not connection in route) or connection == "end" or connection.isupper():
                    routes.append(route + [connection])
            elif part == 2:
                if (connection.islower() and connection != "start" and not (hasSmallDuplicates(route) and connection in route)) or connection == "end" or connection.isupper():
                    routes.append(route + [connection])
        routes.remove(route)

    routes = []
    completedRoutes = []

    routes.append (["start"])

    while len(routes) > 0:
        for i,r in enumerate(routes):
            if r[-1] != "end":
                addConnections(routes,r)
            else:
                completedRoutes.append(r)
                routes.pop(i)
            if len(completedRoutes) % 1000 == 0:
                    print(len(routes),"working,",len(completedRoutes),"completed.")

    return completedRoutes

if __name__ == "__main__":

    lines = load("input12.txt")
    connections = loadConnections(lines)
    print (connections)

    #Solve Part 1
    routes = findRoutes(connections,1)

    #Solve Part 2
    routes2 = findRoutes(connections,2)
    print("PART 1:", len(routes))
    print("PART 2:", len(routes2))