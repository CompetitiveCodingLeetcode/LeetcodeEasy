import unittest
from typing import List

from Searching.BinarySearch.findFirstAndLastOccurrence import findFirstOccurrence, findLastOccurrence


def findTotalOccurrences(arr: List[int],n: int,key: int) -> int:
    firstOccurrence = findFirstOccurrence(arr,n,key)
    lastOccurrence = findLastOccurrence(arr,n,key)

    if firstOccurrence == -1 and lastOccurrence == -1:
        return 0
    totalOccurences = lastOccurrence-firstOccurrence+1
    return totalOccurences


class TestTotalOccurrence(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(3, findTotalOccurrences([1, 2, 2,2,3, 5], 6, 2))

    def test_no_match(self):
        self.assertEqual(0, findTotalOccurrences([1, 3, 4, 24],4, 5))

    def test_case2(self):
        self.assertEqual(3, findTotalOccurrences([1, 7,7,7,8,9,10,11], 8, 7))

    def test_case3(self):
        self.assertEqual(2, findTotalOccurrences([1, 3, 7,7,8,9,10,11], 8,7))

    def test_case4(self):
        self.assertEqual(3,findTotalOccurrences([1,2,3,4,5,6,6,6,7],9,6))