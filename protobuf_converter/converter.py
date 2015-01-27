#!/usr/bin/python

import sys

import Result_pb2


def serialize_protobuf(content):
    students = Result_pb2.Result()

    for entry in content:
        details = entry.split(':')
        details = filter(None, details)
        sname = (details[0].split(','))[0]
        rollno = (details[0].split(','))[1]

        student = students.student.add()
        student.name = sname
        student.rollNum = int(rollno)

        details = details[1:]
        for course_entry in details:
            cname = (course_entry.split(','))[0]
            cmarks = (course_entry.split(','))[1]
            course = student.marks.add()
            course.name = cname
            course.score = int(cmarks)

    f = open("result_protobuf", "w+")
    f.write(students.SerializeToString())
    f.close()


def deserialize_protobuf(students):
    content = []

    for student in students.student:
        name = student.name
        rollno = student.rollNum
        entry = name + ',' + str(rollno)

        for course in student.marks:
            entry += ':' + course.name + ',' + str(course.score)

        content.append(entry)
        
    content = '\n'.join(content)
    f = open("output_protobuf.txt", "w+")
    f.write(content)
    f.close()


def main():
    args=sys.argv
    input_file = args[2]


    if args[1] == '-s':
        f = open(input_file, 'r')
        content = f.read()
        content = content.split("\n")
        content = filter(None, content)
        serialize_protobuf(content)

    elif args[1] == '-d':
        students = Result_pb2.Result()
        f = open(input_file, 'r')
        students.ParseFromString(f.read())
        f.close()
        deserialize_protobuf(students)

        
if __name__ == '__main__':
    main()
