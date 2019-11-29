#!/usr/bin/env python3

class Course():
    def __init__(self, _prof, _time, _name, _id, _location, _max_students, _current_students, _credits = 4, _finshed = False):
        self.prof = _prof
        self.time = _time  #This should probably be stored as a string, although it could be in military time
        self.name = _name
        self.id = _id
        self.loc = _location
        self.max_students = _max_students  #integer
        self.students = _current_students  #this is a list of students
        self.credits = _credits
        self.finished = _finshed  
        #I'm not sure if finished should be in students or in courses, because it is possible that we
        #want an unfinished course to be on their record

    def __str__(self):
        return f"Professor: {self.prof},\nTime: {self.time},\nName: {self.name},\nID: {str(self.id)},\n" + \
        f"Location: {self.loc},\nMax: {int(self.max_students)},\nCurrent: {int(self.current_students)}"

    #def add_course(self,
    #Not sure if this should be here on in master list
    #We already have add_course in student

    


a = Course("henry", "now", "The Class", -4, "There", 2**8, 3**4)
print(a)

    
