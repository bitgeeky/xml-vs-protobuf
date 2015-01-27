# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Result.proto',
  package='',
  serialized_pb=_b('\n\x0cResult.proto\"*\n\x0b\x43ourseMarks\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\"E\n\x07Student\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07rollNum\x18\x02 \x01(\x05\x12\x1b\n\x05marks\x18\x03 \x03(\x0b\x32\x0c.CourseMarks\"#\n\x06Result\x12\x19\n\x07student\x18\x01 \x03(\x0b\x32\x08.Student')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COURSEMARKS = _descriptor.Descriptor(
  name='CourseMarks',
  full_name='CourseMarks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CourseMarks.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='CourseMarks.score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=58,
)


_STUDENT = _descriptor.Descriptor(
  name='Student',
  full_name='Student',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Student.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rollNum', full_name='Student.rollNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='marks', full_name='Student.marks', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=129,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='student', full_name='Result.student', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=166,
)

_STUDENT.fields_by_name['marks'].message_type = _COURSEMARKS
_RESULT.fields_by_name['student'].message_type = _STUDENT
DESCRIPTOR.message_types_by_name['CourseMarks'] = _COURSEMARKS
DESCRIPTOR.message_types_by_name['Student'] = _STUDENT
DESCRIPTOR.message_types_by_name['Result'] = _RESULT

CourseMarks = _reflection.GeneratedProtocolMessageType('CourseMarks', (_message.Message,), dict(
  DESCRIPTOR = _COURSEMARKS,
  __module__ = 'Result_pb2'
  # @@protoc_insertion_point(class_scope:CourseMarks)
  ))
_sym_db.RegisterMessage(CourseMarks)

Student = _reflection.GeneratedProtocolMessageType('Student', (_message.Message,), dict(
  DESCRIPTOR = _STUDENT,
  __module__ = 'Result_pb2'
  # @@protoc_insertion_point(class_scope:Student)
  ))
_sym_db.RegisterMessage(Student)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'Result_pb2'
  # @@protoc_insertion_point(class_scope:Result)
  ))
_sym_db.RegisterMessage(Result)


# @@protoc_insertion_point(module_scope)
