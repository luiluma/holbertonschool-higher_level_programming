#!/usr/bin/python3
""" function that returns True if the object is exactly an
        instance of the specified class
    """


def is_same_class(obj, a_class):
    """ is same class definition
    Args:
        obj: an object
        a_class: a type class to check
    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False
    """
    return type(obj) is a_class
