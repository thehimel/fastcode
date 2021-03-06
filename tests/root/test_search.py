import pytest
from src.root.search.binary import binary_search

def test_binary():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    index = 6

    assert binary_search(array, target) == index


def test_binary_not_found():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 100
    index = -1

    assert binary_search(array, target) == index
