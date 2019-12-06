#!/usr/bin/env python3
class Queue(): #{{{
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):  #O(1)
        self.items.append(item)

    def dequeue(self): #O(n)
        if len(self.items) is not 0:
            a = self.items[0]
            self.items = self.items[1:]
            return a
        else:
            return None
    
    def is_empty(self): #O(1)
        return (len(self.items) is 0)
#}}}
class Student():  #{{{
    def __init__(self, _name, _unused_id):
        self.name = _name        #string
        self.courses = []        #List of course objects
        self.id = _unused_id     #Integer

    def __str__(self):
        return f"Name = {self.name},\nCourses = {str(self.courses)},\nID = {str(self.id)}"

    def add_course(self, new_course):
        self.courses.append(new_course)

    #def drop_course(self, course_to_remove):  #Don't use this anymore, just remove student from course
    #    self.courses.remove(course_to_remove) #Not sure if the remove method works here, make sure to test this later

    def get_credits(self):
        credits = 0
        for course in self.courses:
            if course.finished is True:  #Make sure not to add unfinished courses to credits
                credits += course.credits
        return credits #This wouldn't be too hard to do with recursion
    #}}}
class Course():  #{{{
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
        self.queue_to_enter = Queue()   
        
        self.course_id = self.dept + self.number + "-" +  self.section

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
    #}}}
class MasterListCourses():
    def __init__(self):
        self.course_list = []

    def __str__(self):
        return str(self.course_list)
    
    def add_course(self, _title, _dept, _number, _credits = 4):
        a = MasterCourse(_title, _dept, _number, _credits)
        self.course_list.append(a)

    def add_to_current(self, current_courses, master_to_add, _prof, _time, _location, _max_students, _term, _section):
        current_courses.append(master_to_add


    def remove_course(self, _dept, _number):
        i = 0
        found = False
        while i < self.course_list:
            if self.course_list[i].dept is _dept and self.course_list[i].number is _number:
                self.course_list.pop(i)
                found = True
            i += 1

class MasterCourse():
    def __init__(self, _title, _dept, _number, _credits = 4):
        self.title = _title
        self.dept = _dept
        self.number = _number
        self.credits = _credits
    
    def __str__(self):
        return self.dept + self.number + ": " + self.title

#Tests {{{
 #def __init__(self, _prof, _time, _title, _dept, _number, _location, _max_students, _term, _section, _credits = 4):
a = Course("Shad", "1:30-2:30", "Algorithms and Data Structures", "CS", "160", "Olin 202", 2, "F2019", "A")
#print(a)
#def __init__(self, _name, _unused_id):
b = Student("sdf", 32)
c = Student("dgd", 34)

a.add_student(b)
a.add_student(c)
#print(a.current_students)

a.remove_student(c.id)

for stu in a.current_students:
    print(stu)

print(c)
#}}}
