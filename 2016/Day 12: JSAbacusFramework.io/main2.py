import json

with open('Input.txt', 'r') as myfile:
    content=myfile.read().replace('\n', '')


obj = json.loads(content);

def loop(item):

    if type(item) == dict:
        total = 0;
        if "red" not in item.values():
            for key, value in item.items():
                total += loop(value)
        return total
    if type(item) == int:
        return item
    if type(item) == list:
        total = 0
        for x in item:
             total += loop(x)
        return total
    return 0


print loop(obj)
