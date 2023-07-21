#!/usr/bin/python3
"""Script that computes metrics by reading stdin line by line """

import re
import sys

regex = '(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\\.\
    (?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\\.\
        (?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\\.\
            (?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\
                  - \\[(?:[\\d\\. :-]+)\\] "GET /projects/260 HTTP/1.1" \
                    (200|301|400|401|403|404|405|500) \
                        (102[0-4]|10[0-1][0-9]|[1-9][0-9]{2}|[1-9])'
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

file_size = 0
count = 1
result = []
for line in sys.stdin:
    match = re.search(regex, line)
    if match is None:
        continue
    status = match.group(1)
    if not status.isnumeric():
        del status_codes[status]
        continue
    size = int(match.group(2))
    file_size += size
    status_codes[status] += 1
    count += 1
    if count == 10:
        print(f"File size: {file_size}")
        count = 1
        file_size = 0
        for status, count in status_codes.items():
            if count != 0:
                print(f"{status}: {count}")
        status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                        '403': 0, '404': 0, '405': 0, '500': 0}
