#!/usr/bin/python3
def uppercase(str):
    x = len(str)
    count = 0
    index = 0
    while count < x:
        if ord(str[index]) > 96 and ord(str[index]) < 123:
            print("{:c}".format(ord(str[index]) - 32), end='')
        else:
            print(str[index], end='')
        index = index + 1
        count = count + 1
        if count == x - 0:
            print()
            break
