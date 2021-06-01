#!/usr/bin/python3
""" Module that read a file """


def write_file(filename="", text=""):
    """ Method that write a file and prints len characters

    Return:
            Nothing.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        data = file.write(text)
        return data
