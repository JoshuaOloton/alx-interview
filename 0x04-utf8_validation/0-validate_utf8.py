#!/usr/bin/python3
""" Module for UTF=8 validation """


def validUTF8(data):
    """ Return: True if data is a valid UTF-8 encoding, else return False """
    no_of_bytes = 0
    for byte in data:
        if no_of_bytes == 0:
            if (byte >> 5) == 0b110:
                no_of_bytes = 1
            elif (byte >> 4) == 0b1110:
                no_of_bytes = 2
            elif (byte >> 3) == 0b11110:
                no_of_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            no_of_bytes -= 1
    return no_of_bytes == 0
