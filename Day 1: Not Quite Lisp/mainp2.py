
floor = 0;
answer = 0;

with open('input.txt', 'r') as myfile:
    data=myfile.read()

for i, c in enumerate(data):
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

    if floor == -1:
        print(i+1)
        break
