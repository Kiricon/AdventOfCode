import re

with open("Input.txt") as f:
    content = f.readlines()

class Ingredient:

    def __init__(self, cap, dur, flav, text, cal, name):
        self.capacity = cap
        self.durability = dur
        self.flavor = flav
        self.texture = text
        self.calories = cal
        self.name = name


Ingredients = []
for line in content:

    line = line.replace('\n', '')
    line = line.replace(':', '')
    line = line.replace(',', '')

    arr = line.split(' ')
    Ingredients.append(Ingredient(int(arr[2]), int(arr[4]), int(arr[6]), int(arr[8]), int(arr[10]), arr[0] ))

####### Setup is complete, time for real code

room = 100
realUsed = {}
answer = 0

for ing in Ingredients:
    realUsed[ing.name] = 0


def findTotal(Ingredients, used):
    total = 0
    capTotal = 0
    durTotal = 0
    flavTotal = 0
    textTotal = 0

    for ing in Ingredients:

        usedNo = used[ing.name]
        capTotal += ing.capacity * usedNo
        durTotal += ing.durability * usedNo
        flavTotal += ing.flavor * usedNo
        textTotal += ing.texture * usedNo

    capTotal = capTotal if capTotal > 0 else 0
    durTotal = durTotal if durTotal > 0 else 0
    flavTotal = capTotal if capTotal > 0 else 0
    textTotal = textTotal if textTotal > 0 else 0

    return capTotal * durTotal * flavTotal * textTotal

def loop(total, used):
    global answer
    global room
    if total < room:
        for ing in Ingredients:

            newTotal = total
            newUsed = used.copy()

            newUsed[ing.name] += 1
            newTotal +=1

            if findTotal(Ingredients, newUsed) > 0 or newTotal < 4:
                loop(newTotal, newUsed)

    else:

        total = findTotal(Ingredients, used)

        if total > answer:
            answer = total
            print "----------"
            print answer
            print used


loop(0, realUsed)

print answer
