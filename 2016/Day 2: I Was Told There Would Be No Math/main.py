totalArr = [];
totalAnswer = 0;
with open("Input.txt") as f:
    for line in f.readlines():
        totalArr.append(line.replace('\n', "").split("x"))


for arr in totalArr:
    smallest = 0
    smallestIndex = 0
    for i,val in enumerate(arr):
        arr[i] = int(val)

    answer = 2*arr[0]*arr[1] + 2*arr[1]*arr[2] +2*arr[2]*arr[0];

    for i, val in enumerate(arr):
        if(i != len(arr)-1):
            if(val* arr[i+1] > smallest):
                smallest = val * arr[i+1]
        else:
            if(val * arr[0] > smallest):
                smallest = val * arr[0]

    for i, val in enumerate(arr):
        if(i != len(arr)-1):
            if(val* arr[i+1] < smallest):
                smallest = val * arr[i+1]
        else:
            if(val * arr[0] < smallest):
                smallest = val * arr[0]

    totalAnswer += answer + smallest;



print(totalAnswer)
