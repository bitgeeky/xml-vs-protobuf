#!/usr/bin/python

import sys
import time

import Result_pb2

record_count = 0

def serialize_protobuf(content):
    students = Result_pb2.Result()

    for entry in content:
        global record_count
        record_count += 1
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

    return students


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
    return content


def main():
    args=sys.argv
    input_file = args[2]


    if args[1] == '-s':
        f = open(input_file, 'r')
        content = f.read()
        content = content.split("\n")
        f.close()

        content = filter(None, content)
        students = serialize_protobuf(content)
        f = open("result_protobuf", "w+")
        f.write(students.SerializeToString())
        f.close()

    elif args[1] == '-d':
        students = Result_pb2.Result()
        f = open(input_file, 'r')
        students.ParseFromString(f.read())
        f.close()
        content = deserialize_protobuf(students)
        f = open("output_protobuf.txt", "w+")
        f.write(content)
        f.close()

    elif args[1] == '-t':
        global record_count
        record_count = 0

	start_time = time.time()

        text_file = args[2]
        f = open(text_file, 'r')
        content = f.read()
        data_size = sys.getsizeof(content)
        content = content.split("\n")
        f.close()
        content = filter(None, content)
        students = serialize_protobuf(content)
        
        protobuf_file = args[3]
        students = Result_pb2.Result()
        f = open(protobuf_file, 'r')
        students.ParseFromString(f.read())
        f.close()
        content = deserialize_protobuf(students)
        
        total_time = time.time() - start_time

        print "Average Record Size: " + str(data_size/record_count) + "bytes"
        print "Total time for serialization and deserialization: " + str(total_time * 1000) + " ms"
        print "Rate of serialization/deserialization: " + str((data_size * 1000)/ (total_time * 1024 * 1024)) + " Mbps"

        
if __name__ == '__main__':
    main()
