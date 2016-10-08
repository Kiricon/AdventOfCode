with open('Input.txt', 'r') as myfile:
    content=myfile.read().replace('\n', '')

answer = ''
# boolean returning function to tell us if it's valid or not
def isValid(string):

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
        last = c

    if strait == 3 and doubles == 2:
        return True
    else:
        return False

def characterLoop(i, string):

    spot = string[i]
    original = string[i]

    a = 97
    z = 122

    for c in range(ord(original), z+1):
        temp = list(string)
        temp[i] = chr(c)
        string = "".join(temp)
        print string
        if isValid(string):
            answer = string
            break;


    for c in range(a, ord(original)):
        temp = list(string)
        temp[i] = chr(c)
        string = "".join(temp)
        print string
        if isValid(string):
            answer = string
            break


characterLoop(0,"m")
newPass = content[::-1]
