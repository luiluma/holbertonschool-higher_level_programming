#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv
    len_args = len(args)
    sum = 0
    for x in range(1, len_args):
        sum += int(args[x])
    print(sum)
