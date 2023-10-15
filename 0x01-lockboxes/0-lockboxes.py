#!/usr/bin/python3
"""
Lockboxes - Check README.md for detailed explanation of the problem.
"""


def canUnlockAll(boxes):
    """
    This algorithm approches the solution to the problem by
    making a recursive call to a function that opens a new box
    every time it is called, with the available keys unlocked from other boxes.
    """

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
    """
    This function tries to open boxes according to the index
    of the key in the all_keys list.
    The index increase, every time the function is called.
    New keys are added to all_keys if the box can be opened,
    and the number of used keys is set to 1 per function call.

    If the key did not open any box, however, used_keys = 0,
    since no keys were used.

    The recursion ends when all the boxes that can be opened
    with the available keys are opened,
    and we have now approached the end of all_keys.
    """
    # base condition
    if index == len(all_keys):
        return 0

    used_keys = 0
    key = all_keys[index]

    if key < len(boxes):
        new = [key for key in boxes[key] if key not in all_keys and key != 0]
        all_keys.extend(new)
        used_keys = 1

    index += 1
    used_keys += get_keys(boxes, all_keys, index)
    return used_keys
