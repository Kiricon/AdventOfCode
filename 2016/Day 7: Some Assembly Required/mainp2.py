
with open("Input.txt") as f:
    content = f.readlines()

dic = {}



def getValue(key):

    line = ""
    for temp in content:
        split = temp.split()
        last = split[len(split)-1]
        if last == key:
            line = temp
            break


    line = line.replace("\n", "")
    val1 = "-1"
    val2 = "-1"
    op= 0
    end = ""

    # Parse this thing out

    arr = line.split()

    if len(arr) == 3:
        val1 = arr[0]
        end = arr[2]
        if val1.isdigit():
            dic[end] = int(val1)
        else:
            if val1 in dic:
                dic[end] = dic[val1]
            else:
                dic[end] = getValue(val1)

    elif len(arr) == 4:

        val1 = arr[1]
        end = arr[3]
        if val1.isdigit():
            dic[end] = (~val1 & 0xffff)
        else:
            if val1 in dic:
                dic[end] = (~dic[val1] & 0xffff)
            else:
                dic[end] = (~getValue(val1) & 0xffff)

    elif len(arr) == 5:

        if arr[0].isdigit():
            val1 = int(arr[0])
        else:
            if arr[0] in dic:
                val1 = dic[arr[0]]
            else:
                val1 = getValue(arr[0])

        op = arr[1]
        if arr[2].isdigit():
            val2 = int(arr[2])
        else:
            if arr[2] in dic:
                val2 = dic[arr[2]]
            else:
                val2 = getValue(arr[2])

        end = arr[4]

        if op == "AND":
            dic[end] = val1 & val2
        elif op == "OR":
            dic[end] = val1 | val2
        elif op == "LSHIFT":
            dic[end] = val1 << val2
        elif op == "RSHIFT":
            dic[end] = val1 >> val2
    return dic[end]

temp = getValue("a")
dic = {}
dic["b"] = temp
print getValue("a")
