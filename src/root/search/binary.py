"""
Binary Search Algorithm (Iterative Solution)
https://github.com/thehimel/data-structures-and-algorithms-udacity/blob/master/m03c01-basic-algorithms/i03e00_binary_search_iterative.py
"""


def binary_search(a, t):
    s, e = 0, len(a) - 1

    while s <= e:
        i = (s + e) // 2
        x = a[i]

        if t is x:
            return i
        elif t < x:
            e = i - 1
        else:
            s = i + 1
    return -1
