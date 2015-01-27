#!/usr/bin/python

import sys

import xml.etree.cElementTree as ET


def serialize_xml(content):
    # Start Building a Tree
    students = ET.Element("students")

    for entry in content:
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
    tree.write("result.xml")


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
    f = open("output_xml.txt", "w+")
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
        serialize_xml(content)

    elif args[1] == '-d':
        tree = ET.parse(input_file)
        deserialize_xml(tree)

        
if __name__ == '__main__':
    main()
