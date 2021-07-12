"""
Binary Search Algorithm (Iterative Solution)
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
