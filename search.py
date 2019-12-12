#!/usr/bin/env python3

def binary_search(li, index, upper_bound, lower_bound, item): #O(log(n))
    if li[index] == item:
        return True
    elif abs(upper_bound - lower_bound) <= 1:
        return False
    elif li[index] > item:
        return binary_search(li, index - (upper_bound-lower_bound)//2, index, lower_bound, item)
    elif li[index] < item:
        return binary_search(li, index + (upper_bound-lower_bound)//2, upper_bound, index, item)
    else:
        return False
