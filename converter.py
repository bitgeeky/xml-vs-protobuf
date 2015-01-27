#!/usr/bin/python

import sys

import xml.etree.cElementTree as ET


args=sys.argv

input_file = args[2]

f = open(input_file, 'r')
content = f.read()
content = content.split("\n")
content = filter(None, content)


def serialize_xml():
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


serialize_xml()
        

