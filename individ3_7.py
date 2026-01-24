#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    mytup = (1, 2, 4, 3, 6, 5)
    print(mytup)

    index = list()
    j = -1
    for i in mytup:
        first = i % 2 ==0
        second = j % 2 == 0
        if first and second:
            index += str(mytup.index(i))
        elif i % 2 == 0 and j % 2 != 0 :
            j = i

    s = int(index[0])
    sli = mytup[0:s + 1]
    print(sli)