with open('Input.txt', 'r') as myfile:
    content=myfile.read().replace('\n', '')

# Our lookSay function to conver the text to the new style
def lookSay(data):
    num = 1
    last = ''
    string = ''
    for i, c in enumerate(data):

        if last == c:
            num += 1
        elif last != '':
            string += str(num)
            string += last
            last = c
            num = 1
        elif last == '':
            last = c

        if i == len(data)-1:
            string += str(num)
            string += last


    return string

#Do it 40 times
for i in range(50):

    content = lookSay(content)

#print the length
print len(content)
