with open("Input.txt") as f:
    content = f.readlines()

routes = []
visited = []
locations = []
path = 0
connections = []

for line in content:
    line = line.replace('\n', ' ')
    route = []
    arr = line.split(' ')

    route.append(arr[0])
    route.append(arr[2])
    route.append(int(arr[4]))

    if route[0] not in locations:
        locations.append(route[0])
    if route[1] not in locations:
        locations.append(route[1])
    routes.append(route)

def findConnection(spot):
    global path
    global visited
    global connections
    smallest = 999
    smallestRoute = []

    for route in routes:
        if spot in route and route[2] < smallest:
            visitNum = 0
            for visit in visited:
                if visit in route:
                    visitNum += 1
            if visitNum == 0:
                connections.append(route)
                visited.append(spot)
                smallest = route[2]
                path += route[2]
                if route[0] == spot:
                    findConnection(route[1])
                else:
                    findConnection(route[0])



finalPath = 9999
finalConnections = []
for spot in locations:

    visited = [];
    path = 0;
    connections = []
    findConnection(spot)

    if path < finalPath:
        finalPath = path
        finalConnections = connections

print finalPath
print finalConnections
