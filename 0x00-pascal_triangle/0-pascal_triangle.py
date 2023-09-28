#!/usr/bin/python3

"""
This module contains a function pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of size n
    """

    if n <= 0:
        return []

    pas_list = [[1]]

    if n > 1:
        pas_index = 0
        while len(pas_list) < n:
            new_list = [1]
            sub_index = 0
            sub_list = pas_list[pas_index]

            while sub_list:
                try:
                    add = sub_list[sub_index] + sub_list[sub_index+1]
                    new_list.append(add)
                    sub_index += 1

                except IndexError:
                    new_list.append(1)
                    break

            pas_index += 1
            pas_list.append(new_list)

    return pas_list
