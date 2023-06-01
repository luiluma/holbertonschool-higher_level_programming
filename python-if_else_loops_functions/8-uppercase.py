#!/usr/bin/Python3
def uppercase(str):
    for upper in range(len(str)):
        if str[upper] >= 'a' and str[upper] <= 'z':
            conv = str[upper]
            conv = ord(conv) - 32
            conv = chr(conv)
            str = str[:upper] + conv + str[upper + 1:]
    print("{}".format(str))
