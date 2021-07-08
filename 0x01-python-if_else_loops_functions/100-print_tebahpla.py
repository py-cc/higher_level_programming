#!/usr/bin/python3
a_range = range(97, 123)
reverser_range = reversed(a_range)
for i in reverser_range:
    char = chr(i)
    if i % 2 == 0:
        print(char, end='')
    else:
        print(char.upper(), end='')
