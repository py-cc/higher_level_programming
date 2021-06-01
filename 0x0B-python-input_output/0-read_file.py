#!/usr/bin/python3
"""Module that read a file"""


def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as f:
        text = f.read()
        print(text, end='')
