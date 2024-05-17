from typing import List


def is_almost_sorted(arr: List):
    allowed = 2
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            allowed -= 1
        if allowed == 0:
            return False
    return True


def test_is_almost_sorted():
    assert is_almost_sorted([]) is True
    assert is_almost_sorted([0]) is True
    assert is_almost_sorted([1, 2, 3, 6, 9]) is True
    assert is_almost_sorted([1, 4, 3, 7, 9]) is True
    assert is_almost_sorted([1, 3, 2, 6, 0]) is False
    assert is_almost_sorted([1, 0, -1, -2, -3]) is False
    assert is_almost_sorted([1, 3, 2, 6]) is True
    assert is_almost_sorted([1, 3, 4, 1]) is True
    assert is_almost_sorted([1, 3, 2, 4, 5, 6, 7, 8]) is True
    assert is_almost_sorted([3, 5, 10, 6, 14]) is True
    assert is_almost_sorted([3, 5, 3, 10, 6, 14]) is False
    assert is_almost_sorted([1, 2, 100, 3, 4, 5]) is True


test_is_almost_sorted()
