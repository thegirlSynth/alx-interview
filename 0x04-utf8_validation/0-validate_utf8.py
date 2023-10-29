#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding, else return is False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data,
    Therefore only the 8 least significant bits of each integer is handled.
    """

    encoding = ("0", "110", "1110", "11110")
    indx = 1

    if data:
        first_byte = bin(data[0])[2:]
        if len(first_byte) < 8:
            first_byte = "0" + first_byte

        for num, encoding_prefix in enumerate(encoding):
            if first_byte.startswith(encoding_prefix):
                while indx < len(data) and num:
                    next_byte = bin(data[indx])[2:]
                    if not next_byte.startswith("10"):
                        return False
                    indx += 1
                    num -= 1

                return True

    return False
