with open("Input.txt") as f:
    content = f.readlines()


nodes = []
people = []

pathTaken = []
answer = 0
answerHistory = []
##### Create list of people
for line in content:
    line = line.replace('\n', '')
    line = line.replace('.', '')
    arr = line.split(' ')

    if arr[0] not in people:
        people.append(arr[0])

#### Create Nodes
for person in people:
    node = {'name': person, 'locs': []}
    for line in content:
        line = line.replace('\n', '')
        line = line.replace('.', '')
        arr = line.split(' ')
        if arr[0] == person:
            loc = {}
            if arr[2] == "gain":
                loc = {'name': arr[10], 'units': int(arr[3])}
            else:
                loc = {'name': arr[10], 'units': -int(arr[3])}
            node.get('locs').append(loc)
    nodes.append(node)

#### Find Node by name
def findNode(name):
    for n in nodes:
        if n.get('name') == name:
            nextNode = n
    return nextNode

#### Find best person to sit next to!
def findBest(node, seated, total, totalHistory):
    for loc in node.get('locs'):
        newTotal = total
        newSeated = seated[:]
        global answer
        global pathTaken
        global answerHistory

        newHistory = totalHistory[:]
        #print loc
        if loc.get('name') not in newSeated:
            ### Find other person's happy
            nextNode = findNode(loc.get('name'))
            other = nextNode
            otherHappy = 0

            for otherLoc in other.get('locs'):
                if node.get('name') == otherLoc.get('name'):
                    otherHappy = otherLoc.get('units')

            happy = loc.get('units') + otherHappy

            newHistory.append(happy)
            newTotal += happy
            newSeated.append(nextNode.get('name'))

            if len(newSeated) == len(people):
                if newTotal > answer:
                    answer = newTotal
                    pathTaken = seated
                    answerHistory = newHistory
            else:
                findBest(nextNode, newSeated, newTotal, newHistory)




## Loop through each node and try a few combos

for node in nodes:

    seated = [node.get('name')]
    total = 0
    totalHistory = []

    findBest(node, seated[:], total, totalHistory[:])


print answer
print answerHistory
print pathTaken
