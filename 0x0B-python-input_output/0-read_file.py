#!/usr/bin/python3
"""Module contains a function that reads a text file"""


def read_file(filename=""):
	"""Reads a text file (UTF8) and prints it to stdout
	
	Args:
		filename (str, optional): [description]. Defaults to "".
		
	Raises:
		Exception: [description]
		
	Returns:
		[type]: [description]
		
	"""

	with open(filename, encoding='utf-8') as file:
		read_data = file.read()
		print(read_data, end="")
