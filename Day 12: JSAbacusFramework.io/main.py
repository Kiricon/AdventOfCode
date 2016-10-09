import re

with open('Input.txt', 'r') as myfile:
    content=myfile.read().replace('\n', '')

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


content = re.sub('[{}:,\[\]""]', ' ', content)

arr = content.split(" ");
answer = 0;

for item in arr:
    if isInt(item):
        answer += int(item);

print answer;
