"""
Binary Search Algorithm (Iterative Solution)
https://github.com/thehimel/data-structures-and-algorithms-udacity/blob/master/m03c01-basic-algorithms/i03e00_binary_search_iterative.py
"""


def binary_search(a, t):
    si, ei = 0, len(a) - 1

    while si <= ei:
        mi = (si + ei) // 2
        me = a[mi]

        if t is me:
            return mi

        elif t < me:
            ei = mi - 1

        else:
            si = mi + 1

    return -1
