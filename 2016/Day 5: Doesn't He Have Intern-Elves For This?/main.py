
lines = ""
nice = 0
vowels = ['a', 'e', 'i', 'o', 'u']

# read in the file
with open("input.txt") as f:
    lines = f.readlines()

#parse each string set
for line in lines:

    line = line.replace('\n', "")

    double = False
    vowelCount = 0
    lastCharacter = ""

    #check if we can diqualify it
    if "ab" not in line and "cd" not in line and "pq" not in line and "xy" not in line:
        for c in line:
            for v in vowels:
                if c == v:
                    vowelCount +=1
            if c == lastCharacter:
                double = True

            lastCharacter = c

        if vowelCount >= 3 and double:
            nice +=1

print(nice)
