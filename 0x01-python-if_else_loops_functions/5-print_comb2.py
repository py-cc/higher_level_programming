#!/usr/bin/python3
for x in range(0, 100):
    if x == 99:
        print("{:d}".format(x))
        break
    else:
        print("{:d}".format(x), end=', ')
