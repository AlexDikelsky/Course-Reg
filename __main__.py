#!/usr/bin/env python3

import course
import master_course_list
import master_course
import queue
import student


master = master_course_list.MasterListCourses()

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


for c in master.course_list:
    print(c)
