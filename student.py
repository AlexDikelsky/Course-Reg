#!/usr/bin/env python3

import sorter
import course

class Student():  
    def __init__(self, _name, _unused_id):
        self.name = _name        #string
        self.courses = []        #List of course objects
        self.id = _unused_id     #Integer

    def __str__(self):
        return f"Name = {self.name},\nCourses = {str(self.courses)},\nID = {str(self.id)}"

    def list_courses(self, ordering):
        if ordering is "dept":
            print(sorter.bubblesort(self.courses.dept))

    def add_course(self, new_course):
        self.courses.append(new_course)

    def drop_course(self, course_to_remove):  #Don't use this anymore, just remove student from course
        self.courses.remove(course_to_remove) #Not sure if the remove method works here, make sure to test this later

    def get_credits(self):
        credits = 0
        for course in self.courses:
            if course.finished is True:  #Make sure not to add unfinished courses to credits
                credits += course.credits
        return credits #This wouldn't be too hard to do with recursion
