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
    route.append(int(arr[4]))

    if route[0] not in locations:
        locations.append(route[0])
    if route[1] not in locations:
        locations.append(route[1])

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
    secondFastest = []

    for path in paths:
        if path[2] <= fastestNum and path[2] not in fastestPaths:
            fastestNum = path[2]
            fastest = path

    paths.remove(fastest)
    #paths = filter(lambda a: a != fastest, paths)

    for path in paths:
        if paths[2] <= secondFastestNum and path[2] not in fastestPaths:
            secondFastestNum = path[2]
            secondFastest = path

    if fastest not in fastestPaths:
            fastestPaths.append(fastest)
    if secondFastest in fastestPaths and edcondFastest != []:
        fastestPaths.append(secondFastest)

print fastestPaths
