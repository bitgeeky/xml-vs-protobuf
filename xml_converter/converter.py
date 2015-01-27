#!/usr/bin/python

import sys
import time

import xml.etree.cElementTree as ET


record_count = 0

def serialize_xml(content):
    # Start Building a Tree
    students = ET.Element("students")

    for entry in content:
        global record_count
        record_count += 1
        details = entry.split(':')
        details = filter(None, details)
        sname = (details[0].split(','))[0]
        rollno = (details[0].split(','))[1]

        student = ET.SubElement(students, "student")
        ET.SubElement(student, "name").text = sname
        ET.SubElement(student, "rollno").text = rollno

        details = details[1:]
        for course in details:
            cname = (course.split(','))[0]
            cmarks = (course.split(','))[1]
            ET.SubElement(student, "course", name=cname, marks=cmarks)

    tree = ET.ElementTree(students)
    return tree


def deserialize_xml(tree):
    students = tree.getroot()
    content = []

    for student in students:
        name = student[0].text
        rollno = student[1].text
        entry = name + ',' + rollno

        courses = student[2:]

        for course in courses:
            entry += ':' + course.attrib['name'] + ',' + course.attrib['marks']

        content.append(entry)
        
    content = '\n'.join(content)
    return content


def main():
    args=sys.argv
    input_file = args[2]


    if args[1] == '-s':
        f = open(input_file, 'r')
        content = f.read()
        f.close()
        content = content.split("\n")
        content = filter(None, content)
        tree = serialize_xml(content)
        tree.write("result.xml")

    elif args[1] == '-d':
        tree = ET.parse(input_file)
        content = deserialize_xml(tree)
        f = open("output_xml.txt", "w+")
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
        f.close()
        content = content.split("\n")
        content = filter(None, content)
        tree = serialize_xml(content)

        xml_file = args[3]
        tree = ET.parse(xml_file)
        content = deserialize_xml(tree)
        
        total_time = time.time() - start_time
        
        print "Average Record Size: " + str(data_size/record_count) + "bytes"
        print "Total time for serialization and deserialization: " + str(total_time * 1000) + " ms"
        print "Rate of serialization/deserialization: " + str((data_size * 1000)/ (total_time * 1024 * 1024)) + " Mbps"


if __name__ == '__main__':
    main()
