# -*- coding: utf-8 -*- 


import sys
import re

# 196.223.28.31 - - [16/Nov/2015:00:00:00 +0400] "GET /photo/manage.cgi HTTP/1.1" 404 0 "-" "Mozilla/6.66"

def main():
    current_key = None
    cnt = 0
    for line in sys.stdin:
        key, value = line.split()
        if current_key is None:
            current_key = key
            cnt = value
        elif current_key != key:
            print current_key, cnt
            current_key = key
            cnt = value
        else:
            cnt += value

    if not current_key is None:
        print current_key, cnt

if __name__ == '__main__':
    main()
