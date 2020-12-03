import itertools as it

with open('Input.txt', 'r') as myfile:
    content=myfile.read().replace('\n', '')


###### boolean returning function to tell us if it's valid or not
def isValid(string):

    string = string[::-1]
    #find it is has illegal characters in it
    if 'i' in string or 'o' in string or 'l' in string:
        return False

    #find if it has 3 character strait
    last = '1'
    strait = 0
    for c in string:
        if c == chr(ord(last)+1):
            strait +=1
            last = c
            if strait == 3:
                break;
        else:
            strait=1
            last = c

    # find it it has any non overlapping doubles
    last = ''
    doubles = 0
    doubleIndex = 0;
    for i, c in enumerate(string):

        if c == last and i != doubleIndex+1:
            doubles += 1
            doubleIndex = i
        last = c

    if strait == 3 and doubles == 2:
        return True
    else:
        return False


##### recursively reverse iterate through the string
def loop(i, string):

    spot = string[i]
    original = string[i]

    a = 97
    z = 122
    for c in it.chain(range(ord(original), z+1), range(a, ord(original))):
        temp = list(string)
        temp[i] = chr(c)
        string = "".join(temp)
        if i-1 >= 0 and loop(i-1, string):
         return True
        if isValid(string):
            answer = string[::-1]
            print answer
            return True

    return False


newPass = content[::-1]
loop( len(newPass)-1, newPass)
