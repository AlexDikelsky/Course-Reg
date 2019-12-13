#!/usr/bin/env python3

import sorter
import course

class Student():  
    def __init__(self, _name, _unused_id): #O(1)
        self.name = _name        #string
        self.courses = []        #List of course objects
        self.id = _unused_id     #Integer

    def __str__(self): #O(1)
        return f"Name = {self.name},\nCourses = {str(self.courses)},\nID = {str(self.id)}"

    def list_courses(self, ordering = None):
        if ordering is "dept":
            print(sorter.bubblesort([x.dept for x in self.courses]))  #O(n²)
        if ordering is None:
            print(sorter.mergesort([x.number for x in self.courses]))  #O(log(n))

    def add_course(self, new_course):  #O(1)
        self.courses.append(new_course)

    def count_credits(self):  #O(n) comple
        total = 0
        for i in self.courses:
            total += i.credits 
        return total


    #def drop_course(self, course_to_remove):  #Don't use this anymore, just remove student from course
    #    self.courses.remove(course_to_remove) #Not sure if the remove method works here, make sure to test this later
