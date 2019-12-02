#!/usr/bin/env python3

class MasterCourseList():
    def __init__(self):
        self.list = []
        self.id = 0

    def create_course(self, prof, time, name, loc, max_stu, credits):
        a = Course(prof, time, name, self.id, loc, max_stu, credits)
        self.list.append(a)
        self.id += 1

    def remove_course(self, id_no):
        #have to use a while loop here because you need to delete a particular
        #element of the list
        found = False
        i = 0
        while i < len(self.list) and not found:
            if self.list[i].id is id_no:
                self.list.pop(i)
                found = True
        #Don't think we need to return anything here





