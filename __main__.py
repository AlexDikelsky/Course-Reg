#!/usr/bin/env python3

import course
import master_course_list
import master_course
import queue
import student


#Start the program by making an empty list of courses
master = master_course_list.MasterListCourses()

#Create a few different classes
master.add_course( \
        master_course.MasterCourse("ZZZThis is at the end of the alphabet",
        "ZZZ", "999"))
master.add_course( \
        master_course.MasterCourse("Algorithms & Data Structures", \
        "CS", "160"))
master.add_course( \
        master_course.MasterCourse("Linear Algebra", \
        "MATH", "240"))
master.add_course( \
        master_course.MasterCourse("Introduction to Health", \
        "HLTH", "100", 1)) 
master.add_course( \
        master_course.MasterCourse("History of Jazz",
        "MUS", "275"))

master.add_course( \
        master_course.MasterCourse("Intro to CS", \
        "CS", "150"))
#

#Make a course starting this semester.
#You have to do master.find_course to make sure that you aren't making a course not in the master list
a = course.Course("Shad", "1:30 MWF", "Olin 202", 24, \
        "F2019", "A", master.find_course( \
        master_course.MasterCourse("Algorithms & Data Structures", \
        "CS", "160"))
        )

b = course.Course("Shelly", "8:00 MWF", "Valders 206", 250, \
        "S2018", "B", master.find_course( \
        master_course.MasterCourse("Introduction to Health", \
        "HLTH", "100", 1))
        )

#This course can have only one student, so you need to register fast
c = course.Course("Guzman", "11:00 MWF", "CFA 123", 1, \
        "S2020", "A", master.find_course( \
        master_course.MasterCourse("History of Jazz",
        "MUS", "275"))
        )

d = course.Course("Zaring", "8:00 MWF", "Olin 202", 250, \
        "S2020", "A", master.find_course( \
        master_course.MasterCourse("Intro to CS", \
        "CS", "150"))
        )

P = student.Student("ZZZZZZx Dikelsky", 404191)
i = student.Student("Alex Dikelsky", 404191)
j = student.Student("Laura Bailey", 12345)

a.add_student(j)
a.add_student(P)
a.add_student(i)
b.add_student(i)
b.add_student(j)
c.add_student(i)  #Alex got into the Jazz class first
c.add_student(j)  #Laura is in the queue, so she can only enter if Alex drops the class
d.add_student(i)

print("This is the list of MasterCourses, simular to those on the Luther Website")

for c in master.course_list:
    print(c)

print()

print("List of courses alex is in:")
for c in i.courses:
    print("Alex: ", c)
print()
print("List of courses Laura is in:")
for c in j.courses:
    print("Laura: ", c)
print("Note that Jazz is not listed")

print()
print("Alex Courses, only list departments. This uses bubblesort")
i.list_courses("dept")
print("Laura Courses, only list the number in order from lowest to highest")
j.list_courses()

print()

print("This is the list of students in Algorithms and Data Structures")
print(a.get_students())

print()
