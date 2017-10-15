# -*- coding: utf-8 -*- 


import sys
import re

# 196.223.28.31 - - [16/Nov/2015:00:00:00 +0400] "GET /photo/manage.cgi HTTP/1.1" 404 0 "-" "Mozilla/6.66"

def main():
    current_key = None
    record_re = re.compile('([\d\.:]+) - - \[(\S+ [^"]+)\] "(\w+) ([^"]+) (HTTP/[\d\.]+)" (\d+) \d+ "([^"]+)" "([^"]+)"')
    for line in sys.stdin:
        match = record_re.match(line)
        #print(match.groups())
        #print(match.group(1))
        if not match:
            continue
        if match.group(6) != "200":
            continue
        print(match.group(1))


if __name__ == '__main__':
    main()
