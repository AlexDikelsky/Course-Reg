#!/usr/bin/env python3

import student
import queue

class Course():  
    def __init__(self, _prof, _time, _location, _max_students, _term, _section, master_course): #{{{
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
        self.credits = master_course.credits
        self.section = _section

        #Names
        self.title = master_course.title
        self.dept = master_course.dept
        self.number = master_course.number

        #Enrollment
        self.current_students = []  #this is a list of students
        self.queue_to_enter = queue.Queue()   
        
        self.course_id = self.dept + self.number + "-" +  self.section
        #}}}

    def __str__(self):
        return self.course_id

    def add_student(self, student):
        if len(self.current_students) >= self.max_students:  #If the class is full
            self.queue_to_enter.enqueue(student)   #Add a student to the overflow queue
        else:
            self.current_students.append(student)  #If it's not, add them to the course
            student.add_course(self)  #also remember to add the student to the course

    def remove_student(self, student_id):
        #have to use a while loop here because you need to delete a particular
        #element of the list
        found = False
        i = 0
        while i < len(self.current_students) and not found:
            if self.current_students[i].id is student_id:
                stu = self.current_students.pop(i)
                stu.drop_course(self)
                found = True
            i += 1
        if found:
            if self.queue_to_enter.is_empty():
                pass
            else:
                self.add_student(self.queue_to_enter.dequeue())
        #Don't think we need to return anything here
    
