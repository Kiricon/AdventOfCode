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
used = []
for ing in Ingredients:
    used.append({'name': ing.name, 'total': room/len(Ingredients)})

switch = 0;
lastTotal = 0;
while switch < len(Ingredients):

    newUsed = used[:]
