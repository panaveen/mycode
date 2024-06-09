#!/usr/bin/python3.6


import sys
import subprocess
import datetime
     
#Checking IP reachability
def ip_reach(iplist):
    for ip in iplist:
        ip = ip.rstrip()
        ping_reply = subprocess.call(['ping', '-c 1', ip], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        if ping_reply == 0:
            print("{} --> Success".format(ip))
            continue
        else:
            print('{} --> Failed'.format(ip))


def main():
    #file = input("Enter the host list: ")
    now = datetime.datetime.now()
    print("Date and time : {}".format(now.ctime()))
    try:
        with open(sys.argv[1], 'r') as f:
            ip_reach(f)
        now = datetime.datetime.now()
        print("Date and time : {}".format(now.ctime()))
    except IndexError:
        print("File is missing")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
