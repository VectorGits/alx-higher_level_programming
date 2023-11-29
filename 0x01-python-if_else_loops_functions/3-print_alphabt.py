#!/usr/bin/python3
print("".join([chr(x) for x in range(97, 123) if chr(x) not in ['q', 'e']]), end='')
