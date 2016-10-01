

visited = []
position = {'x': 0, 'y': 0}
answer = 0

with open('Input.txt', 'r') as myfile:
    data=myfile.read()

for c in data:
    if c == "<":
        position['x'] -= 1
    elif c == ">":
        position['x'] += 1
    elif c == "v":
        position['y'] -= 1
    elif c == "^":
        position['y'] += 1

    if position not in visited:
        visited.append(position.copy())
        answer += 1


print(answer)
