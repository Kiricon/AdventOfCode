
#### Let's build out our grid and populate it with 0s
grid = [];
answer = 0

for row in range(1000):
    newRow = []
    for column in range(1000):
        newRow.append(False)
    grid.append(newRow)

#### Let's read in that file
with open("Input.txt") as f:
    content = f.readlines()


for line in content:

    line = line.replace("\n", "")
    if line.find("turn") != -1:
        line = line.replace("turn ", "")

    arr = line.split(" ")

    command = arr[0]
    start = arr[1].split(",")
    end = arr[3].split(",")

    for x in range(int(start[0]), int(end[0])+1):
        for y in range(int(start[1]), int(end[1])+1):
            if command == "off":
                grid[x][y] = False
            elif command == "on":
                grid[x][y] = True
            elif command == "toggle":
                grid[x][y] = not grid[x][y]


for row in grid:
    for column in row:
        if column == True:
            answer +=1

print answer
