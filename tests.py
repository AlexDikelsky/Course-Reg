#!/usr/bin/env python3
import sorter
import queue

 #def __init__(self, _prof, _time, _title, _dept, _number, _location, _max_students, _term, _section, _credits = 4):
master = MasterListCourses()
master.add_course(MasterCourse("Arbitrary", "NE", "-23"))
master.add_course(MasterCourse("Less arbitrary", "???", "-24"))
master.add_course(MasterCourse("Intro to CS", "CS", "150"))

f = Course("Zaring", "8 MWF", "Olin 202", 22, "F2018", "A", 

f.add_student(Student("Alex", 123))



#a = Course("Shad", "1:30-2:30", "Algorithms and Data Structures", "CS", "160", "Olin 202", 2, "F2019", "A")
##print(a)
##def __init__(self, _name, _unused_id):
#b = Student("sdf", 32)
#c = Student("dgd", 34)
#
#a.add_student(b)
#a.add_student(c)
##print(a.current_students)
#
#a.remove_student(c.id)
#
#for stu in a.current_students:
#    print(stu)
#
#print(c)
