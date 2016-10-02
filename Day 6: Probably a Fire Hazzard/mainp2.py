
#### Let's build out our grid and populate it with 0s
grid = [];
answer = 0

for row in range(1000):
    newRow = []
    for column in range(1000):
        newRow.append(0)
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
                if(grid[x][y] > 0):
                    grid[x][y] -= 1
            elif command == "on":
                grid[x][y] += 1
            elif command == "toggle":
                grid[x][y] += 2


for row in grid:
    for column in row:
        answer += column

print answer
