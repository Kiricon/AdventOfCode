import itertools as it

with open('Input.txt', 'r') as myfile:
    content=myfile.read().replace('\n', '')

answers = []
###### boolean returning function to tell us if it's valid or not
def isValid(string):

    string = string[::-1]
    if content == string:
        return False
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
    if original != z:
        for c in range(ord(original), z+1):
            string[i] = chr(c)
            if isValid("".join(string)):
                answers.append("".join(string)[::-1])
                print string[::-1]
                if len(answers) == 2:
                    answer = "".join(string)[::-1]
                    print answer
                    return True
    else:
        for c in range(a, ord(original)):
            string[i] = chr(c)
            if i-1 >= 0 and loop(i-1, string):
             return True
            if isValid("".join(string)):
                answers.append("".join(string)[::-1])
                print "".join(string)[::-1]
                if len(answers) == 2:
                    answer = "".join(string)[::-1]
                    print answer
                    return True
    return False



newPass = content[::-1]
loop( len(newPass)-1, list(newPass))
