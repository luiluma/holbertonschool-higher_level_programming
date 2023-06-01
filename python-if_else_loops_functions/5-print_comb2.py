#!/usr/bin/python3
for list in range(0, 100):
    if list <= 98:
        print(f'{list:02d}, '.format(list + 1), end="")
    if list > 98:
        print(list, end='\n')
