#!/usr/bin/python3
"""
    Module with a writing function
"""


def write_file(filename="", text=""):
    """
        write_file - writes some text on a file. This overwrites the
        content of the file
    """
    with open(filename, encoding='utf-8', mode='w') as file:
        return(file.write(text))
