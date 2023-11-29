#!/usr/bin/python3
for x in range(0, 9):
	for y in range(x + 1, 10):
		if x < y - 1 or x < 8:
			print("{:d}{:d}, ".format(x, y), end="")
		if x == 8 and y == 9:
			print("{:d}{:d}".format(x, y))
