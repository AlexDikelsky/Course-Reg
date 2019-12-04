#!/usr/bin/env python3
import queue

class Course():
    def __init__(self, _prof, _time, _title, _dept, _number, _location, _max_students, _term, _section, _credits = 4):
        #_prof = Professor  string
        #_time = "1:30-2:30 M/W/F", string
        #_title = "Algorithms and Data Structures", string
        #_dept = "CS", String
        #_number = "160", String
        #_location = "Olin 202"
        #_max_students = 25 Int
        #_term = "F2019" String "S2019"
        #_credits = 32 Int

        #Course Information
        self.prof = _prof
        self.time = _time
        self.term = _term
        self.loc = _location
        self.max_students = _max_students  #integer
        self.credits = _credits

        #Names
        self.title = _title
        self.dept = _dept
        self.number = _number
        self.section = _section

        #Enrollment
        self.current_students = []  #this is a list of students
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
            i += 1
        if found:
            if self.queue_to_enter.is_empty():
                pass
            else:
                self.add_student(self.queue_to_enter.dequeue())
        #Don't think we need to return anything here

a = Course("Shad", "1:30-2:30", "Algorithms and Data Structures", "CS160", "Olin 202", 20, "CS 160", "August 21, 2019")
print(a)

