#!/usr/bin/env python3

import random

def bubblesort(l): #O(n²)
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

def mergesort(alist):  #O(log(n) * n)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        left__index = 0
        right_index = 0
        both__index = 0

        while left__index < len(lefthalf) and right_index < len(righthalf):
            if lefthalf[left__index] < righthalf[right_index]:
                alist[both__index] = lefthalf[left__index]
                left__index += 1
            else:
                alist[both__index] = righthalf[right_index]
                right_index += 1
            both__index += 1

        while left__index < len(lefthalf):
            alist[both__index] = lefthalf[left__index]
            left__index += 1
            both__index += 1

        while right_index < len(righthalf):
            alist[both__index] = righthalf[right_index]
            right_index += 1
            both__index += 1

    return alist

#d = [5, 2, 9, 1, 7, 3]
#d=[2, 3]
#d = ["a", "b", "d", "r", "c"]
#
#print(mergesort(d))

#f = [2, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#f = ["a", "f", "c"]
#print(bubblesort(f))
