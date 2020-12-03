
lines = ""
nice = 0
vowels = ['a', 'e', 'i', 'o', 'u']

# read in the file
with open("input.txt") as f:
    lines = f.readlines()

#parse each string set
for line in lines:

    line = line.replace('\n', "")

    repeats = False
    hasPair = False

    for i, c in enumerate(line):
        #Find if there is a repeat
        if i > 2 and c == line[i-2]:
            repeats = True

        if i < len(line)-1:
            sub = line.rfind(c+line[i+1])
            if sub != -1 and sub != i and sub != i+1:
                hasPair = True


    if hasPair and repeats:
        nice += 1



print(nice)
