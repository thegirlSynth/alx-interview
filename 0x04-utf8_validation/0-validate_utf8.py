#!/usr/bin/python3
"""
UTF-8 Validation
"""


from typing import List, Optional


def validUTF8(data: List[int], verbose: Optional[bool] = False) -> bool:
    """
    param data: A list of integers that represent the binary data to
                be parsed.
    return: True if data is in a valid UTF-8 format, False otherwise
    """
    if not isinstance(data, list) or False in [
        isinstance(x, int) for x in data
    ]:  # noqa
        return False

    # Validate data byte-by-byte and return False if an invalid byte is found
    continuation_bytes = 0
    previous_byte = 0
    for num in data:
        # Convert integer to byte/eight least significant bits (256 == 2^8)
        num %= 256

        # Print verbose output
        if verbose:
            left = continuation_bytes
            print(f"{num}[{left}], " if left else f"{num}, ", end="")

        if num >= 248:
            # Invalid byte -> 248 to 255 > maximum 247 '11110111' for UTF-8
            return False
        # if num in (192, 193, 224, 225):
        if num in (192, 193):
            # Leading bytes for overlong encodings -> '11000000' and '11000001'
            return False
        if num == 128 and previous_byte in (224, 240):
            # Overlong encoding -> '11100000 10000000' or '11110000 10000000'
            return False
        if num < 128:
            # Continuation byte '10xxxxxx' expected but not found '0xxxxxxx'
            if continuation_bytes:
                return False
            # Valid 8-bit/byte character expected/found. Move on to next byte
        elif num < 192:
            # Continuation byte '10xxxxxx' provided but not expected
            if not continuation_bytes:
                return False
            # Continuation byte found, update remainder
            continuation_bytes -= 1
        elif num >= 194:
            # Continuation byte '10xxxxxx' expected but not found '11xxxxxx'
            if continuation_bytes:
                return False
            # Leading byte found. Get length/number of continuation bytes
            continuation_bytes = len(bin(num)[2:].split("0")[0]) - 1
        # Track current byte for overlong encodings checks
        previous_byte = num

    # Return True if sequence ended as expected, else False
    return True if not continuation_bytes else False
