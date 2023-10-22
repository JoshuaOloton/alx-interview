#!/usr/bin/python3
"""Script that computes metrics by reading stdin line by line """

import re
import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

file_size = 0
count = 1
result = []
for line in sys.stdin:
    formatted_line = line.split()
    formatted_line = formatted_line[::-1]
    size = formatted_line[0]
    file_size += int(size)
    status_code = formatted_line[1]
    status_codes[status_code] += 1
    if count == 10:
        print(f"File size: {file_size}")
        for status, count in status_codes.items():
            if count != 0:
                print(f"{status}: {count}")
        status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                        '403': 0, '404': 0, '405': 0, '500': 0}
        file_size = 0
        count = 1
    count += 1
