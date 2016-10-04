with open("Input.txt") as f:
    content = f.readlines()

routes = []
visited = []
locations = []

for line in content:
    line = line.replace('\n', ' ')
    route = []
    arr = line.split(' ')

    route.append(arr[0])
    route.append(arr[2])
    route.append(arr[4])

    if route[0] not in locations:
        locations.append(route[0])
    if route[1] not in locations:
        locations.append(route[0])

    routes.append(route)

loop = True
fastestPaths = [];
#find shortest two paths
for spot in locations:

    paths = []

    for route in routes:
        if spot in route:
            paths.append(route)

    fastestNum = 99999
    fastest = []
    secondFastestNum = 99999
    sedcondFastest = []

    for path in paths:
        if path[2] < fastestNum:
            fastestNum = path[2]
            fastest = path

    paths.remove(fastest)

    for path in paths:
        if paths[2] < secondFastestNum:
            secondFastestNum = path[2]
            sedcondFastest = path

    fastestPaths.append(fastest)
    fastestPaths.append(sedcondFastest)

print fastestPaths
