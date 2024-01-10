#!/usr/bin/python3
"""Module contains a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
	"""Function that returns the dictionary description
	with simple data structure (list, dictionary, string, integer and boolean)
	for JSON serialization of an object

	Arguments:
		obj (object): object to be serialized

	Returns:
		dict: dictionary description of object
	"""

	return obj.__dict__