#!/usr/bin/env python3

import course
import sorter
import search

class MasterListCourses(): 
    def __init__(self):
        self.course_list = []

    def __str__(self):
        return str(self.course_list)
    
    def add_course(self, new_course):
        self.course_list.append(new_course)

    def find_course(self, to_add):
        #Creates a list of course "ids"
        li = [x.title + x.dept + str(x.number) for x in self.course_list]
        #Creates id for thing to look for
        item = to_add.title + to_add.dept + str(to_add.number)
        #print(li, item)
        #Search
        x = search.binary_search(sorter.mergesort(li), \
                len(li)//2, len(li), 0, item)
        if x:
            return to_add
        else:
            print("Attempted to add a course not in the master list")
            return None

    def remove_course(self, to_remove):
        i = 0
        found = False
        while i < len(self.course_list):  #This measures equality between the removed one and the to remove one
            if to_remove.dept is self.course_list[i].dept \
                    and to_remove.title is self.course_list[i].title \
                    and to_remove.number is self.course_list[i].number \
                    and to_remove.credits is self.course_list[i].credits:
                self.course_list.pop(i)
                found = True
            i += 1
        if not found:
            print("Course was not found in the master list")

