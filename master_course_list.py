#!/usr/bin/env python3

class MasterCourseList():
    def __init__(self):
        self.list = []

    def create_course(self, prof, time, name, loc, max_stu, credits, code):
        self.list.append(Course(prof, time, name, loc, max_stu, credits, code))
        
    def remove_course(self, code_to_remove):
        #have to use a while loop here because you need to delete a particular
        #element of the list
        found = False
        i = 0
        while i < len(self.list) and not found:
            if self.list[i].code is code_to_remove:
                self.list.pop(i)
                found = True
            i += 1
        #Don't think we need to return anything here
