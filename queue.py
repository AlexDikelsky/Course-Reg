#!/usr/bin/env python3

class Queue():
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) is not 0:
            a = self.items[0]
            self.items = self.items[1:]
            return a
        else:
            return None
    
    def is_empty(self):
        return (len(self.items) is 0)


        
#a = Queue()
#a.enqueue(4)
#a.enqueue(5)
#print(a.is_empty())
#print(a.dequeue())
#print(a.dequeue())
#print(a.dequeue())
#print(a.is_empty())
