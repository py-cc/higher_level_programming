#!/usr/bin/python3
""" Module that append into a file"""


def append_write(filename="", text=""):
    """ Method that creates and appends a string to a file.

        Returns:
            The numbers of characters written.
    """

    with open(filename, mode='a', encoding='utf-8') as file:
        data = file.write(text)
    return data
