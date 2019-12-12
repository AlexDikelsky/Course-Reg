#!/usr/bin/env python3

import course
import master_course_list
import master_course
import queue
import student


master = master_course_list.MasterListCourses()

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
#

a = course.Course("Shad", "1:30 MWF", "Olin 202", 24, \
        "F2019", "A", master.find_course( \
        master_course.MasterCourse("Algorithms & Data Structures", \
        "CS", "160"))
        )

#b = course.Course("Shelly", "8:00 MWF", "Valders 206", 250, \
#        "S2018", "B", master.find_course( \
#        master_course.MasterCourse("Introduction to Health", \
#        "HLTH", "100", 1))
#        )
#
#c = course.Course("Guzman", "11:00 MWF", "CFA 123", 1, \
#        "S2020", "A", master.find_course( \
#        master_course.MasterCourse("History of Jazz",
#        "MUS", "275"))
#        )
#
#i = student.Student("Alex Dikelsky", 404191)
#j = student.Student("Laura Bailey", 12345)
#
#a.add_student(i)
#a.add_student(j)
#b.add_student(i)
#b.add_student(j)
#c.add_student(i)
#c.add_student(j)
#
#
#for c in i.courses:
#    print("Alex: ", c)
#print()
#for c in j.courses:
#    print("Laura: ", c)
#
#print()
#i.list_courses("dept")
#j.list_courses("dept")


#for c in master.course_list:
#    print(c)
