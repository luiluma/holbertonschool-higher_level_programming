#!/usr/bin/python3
""" method to check inheritance """


def inherits_from(obj, a_class):
    """method definition returns True or False"""
    return isinstance(obj, a_class) and type(obj) is not a_class
