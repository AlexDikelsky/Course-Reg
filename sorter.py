#!/usr/bin/env python3

def bubblesort(l):
    i = 0
    while i < len(l) - 1:
        j = 0
        while j < len(l)-1:
            if l[j] > l[j+1]:
                swap = l[j]
                l[j] = l[j+1]
                l[j+1] = swap
            j += 1
        i += 1
    return l

#f = [2, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#f = ["a", "f", "c"]
#print(bubblesort(f))
