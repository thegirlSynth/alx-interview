#!/usr/bin/python3
"""
Lockboxes - Check README.md for detailed explanation of the problem.
"""

from collections import deque


def canUnlockAll(boxes):
    """
    In this second version of the solution algorithm, the data structure
    of choice is the queue. The first version had the disadvantage of
    getting a maximum recursion depth error for a large number of boxes.

    This approach absolves the need to use a deep recursive function,
    and since it is  not advisable to mutate a list while iterating over it,
    the queue became the next perfect data structure of choice.
    """

    all_keys = deque([0])
    used_keys = set()

    if len(boxes) > 1:
        while all_keys:
            key = all_keys.popleft()

            if key < len(boxes):
                used_keys.add(key)
                new = set(
                    [
                        num
                        for num in boxes[key]
                        if num not in used_keys and num not in all_keys
                    ]
                )
                all_keys.extend(new)

    if len(used_keys) == len(boxes):
        return True
    else:
        return False
