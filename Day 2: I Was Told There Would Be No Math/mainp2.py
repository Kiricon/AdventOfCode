totalArr = [];
totalAnswer = 0;

with open("Input.txt") as f:
    for line in f.readlines():
        totalArr.append(line.replace('\n', "").split("x"))


for arr in totalArr:

    largest = 0
    largestIndex = 0

    for i,val in enumerate(arr):
        arr[i] = int(val)

    ribbon = 0;
    bow = 1;

    for i, val in enumerate(arr):
        if val > largest:
            largest = val
            largestIndex = i


    for i, val in enumerate(arr):

        if i != largestIndex:
            ribbon += val *2

        bow *= val
    totalAnswer += ribbon+bow



print(totalAnswer)
