#!/usr/bin/env python3


import course

class MasterCourse(): 
    def __init__(self, _title, _dept, _number, _credits = 4):
        self.title = _title
        self.dept = _dept
        self.number = _number
        self.credits = _credits
    
    def __str__(self):
        return self.dept + self.number + ": " + self.title

