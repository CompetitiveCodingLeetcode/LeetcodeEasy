import unittest
from typing import List


def binary_search(arr: List[int], target: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return -1


class TestBinarySearch(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(3, binary_search([1, 2, 3, 5], 5))

    def test_no_match(self):
        self.assertEqual(-1, binary_search([1, 3, 4, 24], 5))

    def test_element_found_in_beginning(self):
        self.assertEqual(0, binary_search([1, 2, 3, 23], 1))

    def test_element_found_in_end(self):
        self.assertEqual(3, binary_search([1, 2, 3, 6], 6))
