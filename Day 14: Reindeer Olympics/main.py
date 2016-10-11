with open("Input.txt") as f:
    content = f.readlines()

class Deer:

    def __init__(self, name, km, fTime,rTime):
        self.name = name
        self.km = km
        self.flyTime = fTime
        self.flyCounter = 0
        self.restTime = rTime
        self.restCounter = 0
        self.justFlew = False
        self.totalDistance = 0

# Setup our deers!
deers = []

for line in content:
    line = line.replace('\n', '');
    arr = line.split(' ')

    deer = Deer(arr[0], int(arr[3]), int(arr[6]), int(arr[13]))
    deers.append(deer)

seconds = 2503

##### Race!!
for i in range(seconds):
    for deer in deers:

        if deer.justFlew == False and deer.flyCounter == 0 and deer.restCounter == 0:

            deer.flyCounter = deer.flyTime
            deer.totalDistance += deer.km
            deer.justFlew = True

        elif deer.justFlew == True and deer.flyCounter > 0:
            deer.totalDistance += deer.km

        elif deer.justFlew == True and deer.flyCounter == 0:
            deer.justFlew = False
            deer.restCounter = deer.restTime


        if deer.flyCounter > 0:
            deer.flyCounter -= 1

        if deer.restCounter > 0:
            deer.restCounter -= 1


winner = 0;
for deer in deers:
    print "----------"
    print deer.name +" : "+ str(deer.totalDistance)
    if deer.totalDistance > winner:
        winner = deer.totalDistance

print "#####################"
print "WINNER : "+ str(winner)
