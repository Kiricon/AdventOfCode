import re

with open("Input.txt") as f:
    content = f.readlines()

totalCode = 0
totalString = 0

for line in content:
    line = line.replace('\n', "")

    code = len(line)
    totalCode += code
    string = 0

    line = line[1:-1]
    line = line.replace('\\"', '1')
    line = line.replace('\\\\', '1')
    line = re.sub('\\\\x\S\S', '?', line)

    print line

    string = len(line)
    totalString += string

print totalCode - totalString
