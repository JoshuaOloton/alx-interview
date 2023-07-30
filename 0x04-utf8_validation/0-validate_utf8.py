#!/usr/bin/python3
""" Module for UTF=8 validation """


def validUTF8(data):
    """ Return: True if data is a valid UTF-8 encoding, else return False """
    i = 0
    while i < len(data):
        if (data[i] & 0b10000000) == 0b00000000:
            i += 1
        elif (data[i] & 0b11100000) == 0b11000000:
            if i + 1 >= len(data) or (data[i + 1] & 0b11000000) != 0b10000000:
                return False
            i += 2
        elif (data[i] & 0b11110000) == 0b11100000:
            if i + 2 >= len(data) or \
                    (data[i + 1] & 0b11000000) != 0b10000000 or \
                    (data[i + 2] & 0b11000000) != 0b10000000:
                return False
            i += 3
        elif (data[i] & 0b11111000) == 0b11110000:
            if i + 3 >= len(data) or \
                    (data[i + 1] & 0b11000000) != 0b10000000 or \
                    (data[i + 2] & 0b11000000) != 0b10000000 or \
                    (data[i + 3] & 0b11000000) != 0b10000000:
                return False
            i += 4
        else:
            return False

    return True
