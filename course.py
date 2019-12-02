#!/usr/bin/env python3
import queue

class Course():
    def __init__(self, _prof, _time, _name, _id, _location, _max_students, _credits = 4):
        self.prof = _prof
        self.time = _time  #This should probably be stored as a string, although it could be in military time
        self.name = _name
        self.id = _id
        self.loc = _location
        self.max_students = _max_students  #integer
        self.current_students = []  #this is a list of students
        self.credits = _credits
        self.queue_to_enter = queue.Queue()

    def __str__(self):
        return f"Professor: {self.prof},\nTime: {self.time},\nName: {self.name},\nID: {str(self.id)},\n" + \
        f"Location: {self.loc},\nMax: {int(self.max_students)},\nCurrent: {int(self.current_students)}," + \
        f"\nQueue to enter: {self.queue_to_enter}"

    def add_student(self, student):
        if len(current_students) > max_students:  #If the class is full
            self.queue_to_enter.enqueue(student)  
        else:
            self.current_students.append(student)

    def remove_student(self, id_no):
        #have to use a while loop here because you need to delete a particular
        #element of the list
        found = False
        i = 0
        while i < len(self.current_students) and not found:
            if self.current_students[i].id is id_no:
                self.current_students.pop(i)
                found = True
        #Don't think we need to return anything here


#a = Course("henry", "now", "The Class", -4, "There", 2**8, 3**4)
#print(a)

    
