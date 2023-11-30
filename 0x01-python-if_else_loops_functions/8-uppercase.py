#!/usr/bin/python3
def uppercase(str):
    print("".join([chr(ord(x) - 32) if 97 <= ord(x) <= 122 
                    else x for x in str]))
