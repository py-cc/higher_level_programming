#!/usr/bin/python3
a_range = range(97, 123)
reverser_range = reversed(a_range)
for i in reverser_range:
    if i % 2 == 0:
        print("{:s}".format(chr(i)), end='')
    else:
        print("{:s}".format(chr(i).upper()), end='')
