#!/usr/bin/python3.6

import re

def find_ip(string):
    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    for x in string:
        match = re.findall(pattern, x)
        print(match[0])

def main():
    file = input("Enter file name: ")
    f = open(file, 'r')
    find_ip(f)
    f.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
