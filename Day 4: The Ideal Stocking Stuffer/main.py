import hashlib

text = "iwrupvqb"

loop = True
i = 0

while loop:
    hexHash = hashlib.md5(text+str(i)).hexdigest()
    if hexHash[:5] == "00000":
        loop = False
        print i
    else:
        i +=1
