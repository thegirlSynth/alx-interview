#!/usr/bin/python3
"""
"""


def canUnlockAll(boxes):
    """ """

    all_keys = []
    used_keys = 1

    all_keys.extend(boxes[0])

    if len(boxes) > 1:
        used_keys += get_keys(boxes, all_keys)

    if used_keys == len(boxes):
        return True
    else:
        return False


def get_keys(boxes, all_keys, index=0):
    # base condition
    if index == len(all_keys):
        return 0

    used_keys = 0
    key = all_keys[index]

    if key < len(boxes):
        new_keys = [key for key in boxes[key] if key not in all_keys and key != 0]
        all_keys.extend(new_keys)
        used_keys = 1

    index += 1
    used_keys += get_keys(boxes, all_keys, index)
    return used_keys
