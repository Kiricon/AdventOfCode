with open("Input.txt") as f:
    content = f.readlines()

routes = []
locations = []
nodes = []
global visited
global path
answer = -1

# Get locations and routes
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

# build out nodes
for spot in locations:

    node = {'name': spot, 'locs' : []}


    for route in routes:

        if spot in route:
            if route[0] == spot:
                rname = route[1]
            else:
                rname = route[0]
            node.get('locs').append({'name': rname, 'dist':route[2]})
    nodes.append(node);


# Function for recursivly searching through nodes
def findNearest(node):

    smallest = 999
    name = ""
    global path
    global visited

    for loc in node.get('locs'):

        if loc.get('name') not in visited:
            if loc.get('dist') < smallest:
                smallest = loc.get('dist')
                name = loc.get('name')

    if name != "":
        visited.append(name)
        path += smallest
        for n in nodes:
            if n.get('name') == name:
                findNearest(n)


# Loop through our nodes
for node in nodes:

    visited = [node.get('name')];
    path = 0;
    findNearest(node)

    if answer == -1:
        answer = path
    else:
        if path < answer:
            answer = path


print answer
