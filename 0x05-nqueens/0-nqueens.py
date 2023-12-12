#!/usr/bin/python3
'''N Queens Challenge'''

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            exit(1)
    except ValueError:
        print('N must be a number')
        exit(1)

    solutions = []
    queens_placed = []  # coordinates format [row, column]
    stop = False
    r = 0
    c = 0

    # row iteration
    while r < n:
        re_start = False
        # column iteration
        while c < n:
            # check is current column is safe
            safe = True
            for cordinate in queens_placed:
                col = cordinate[1]
                if (col == c or col + (r-cordinate[0]) == c or
                        col - (r-cordinate[0]) == c):
                    safe = False
                    break

            if not safe:
                if c == n - 1:
                    re_start = True
                    break
                c += 1
                continue

            # place queen
            cordinates = [r, c]
            queens_placed.append(cordinates)
            # if last row, append solution and reset all to last unfinished row
            # and last safe column in that row
            if r == n - 1:
                solutions.append(queens_placed[:])
                for cordinate in queens_placed:
                    if cordinate[1] < n - 1:
                        r = cordinate[0]
                        c = cordinate[1]
                for i in range(n - r):
                    queens_placed.pop()
                if r == n - 1 and c == n - 1:
                    queens_placed = []
                    stop = True
                r -= 1
                c += 1
            else:
                c = 0
            break
        if stop:
            break
        # on fail: go back to previous row
        # and continue from last safe column + 1
        if re_start:
            r -= 1
            while r >= 0:
                c = queens_placed[r][1] + 1
                del queens_placed[r]  # delete previous queen coordinates
                if c < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    for idx, val in enumerate(solutions):
        print(val)
