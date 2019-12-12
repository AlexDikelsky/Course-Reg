#!/usr/bin/env python3

class Queue(): 
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):  #O(1)
        self.items.append(item)

    def dequeue(self): #O(n)
        if len(self.items) is not 0:
            a = self.items[0]
            self.items = self.items[1:]
            return a
        else:
            return None
    
    def is_empty(self): #O(1)
        return (len(self.items) is 0)

