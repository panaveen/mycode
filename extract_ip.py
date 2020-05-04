#!/usr/bin/python3.6

import re

def find_ip(string):
    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    for x in string:
        match = re.findall(pattern, x)
        print(match[0])

f = open('t2_panel', 'r')
find_ip(f)
f.close()

