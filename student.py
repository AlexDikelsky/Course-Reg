#!/usr/bin/env python3


class Student():  
    def __init__(self, _name, _courses, _unused_id):
        self.name = _name        #string
        self.courses = _courses  #List of courses
        self.id = _unused_id     #Integer

    def __str__(self):
        return f"Name = {self.name},\nCourses = {str(self.courses)},\nID = {str(self.id)}"

    def add_course(self, new_course):
        self.courses.append(new_course)

    def drop_course(self, course_to_remove):
        self.courses.remove(course_to_remove) #Not sure if the remove method works here, make sure to test this later

    #def delete_student(self):  This should probably be in the studentlist class
    def get_credits(self):
        credits = 0
        for course in self.courses:
            if course.finished is True:  #Make sure not to add unfinished courses to credits
                credits += course.credits
        return credits #This wouldn't be too hard to do with recursion



#unused_id = 1
#a = Student("Alex", [1, 2], unused_id) 

#Instead of unused_id we should have 
#something in the studentlist class to make sure they
#are unique id numbers

#print(a)
