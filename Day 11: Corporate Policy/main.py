with open('Input.txt', 'r') as myfile:
    content=myfile.read().replace('\n', '')

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


print isValid(content)
