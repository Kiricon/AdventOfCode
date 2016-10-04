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

    line = line.replace('\\', '\\\\')
    line = line.replace('"', '\\"')


    print line

    string = len(line)+2
    totalString += string

print totalString - totalCode
