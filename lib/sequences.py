#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    count = 0
    list = []

    if length <= 0:
        print([])
    elif length == 1:
        list.append(0)
        print(list)
    else:
        while count < length:
            list.append(a)
            c = a + b
            a = b
            b = c
            count+=1
        print(list)