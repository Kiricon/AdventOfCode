
floor = 0;

with open('input.txt', 'r') as myfile:
    data=myfile.read()

floor += data.count('(')
floor -= data.count(')')

print(floor)
