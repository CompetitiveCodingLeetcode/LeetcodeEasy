import unittest
from typing import List


def findFirstOccurrence(arr: List[int],n: int,key: int) -> int:
    low = 0
    high = n-1
    mid = low + int((high-low)/2)
    firstOccurrence = -1
    while low<= high:
        if arr[mid] == key:
            if arr[mid-1] == key:
                high = mid-1
            else:
                firstOccurrence = mid
                break
        elif arr[mid]>key:
            high = mid-1
        else:
            low = mid+1
        mid = low + int((high-low)/2)

    return firstOccurrence

def findLastOccurrence(arr: List[int],n: int,key: int)-> int:
    low = 0
    high = n - 1
    mid = low + int((high - low) / 2)
    lastOccurrence = -1
    while low <= high:
        if arr[mid] == key:
            if arr[mid + 1] == key:
                low = mid + 1
            else:
                lastOccurrence = mid
                break
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
        mid = low + int((high - low) / 2)

    return lastOccurrence

def findFirstAndLastOccurrence(arr: List[int],n:int,key:int)->(int,int):
    firstOccurrence = findFirstOccurrence(arr,n,key)
    lastOccurrence = findLastOccurrence(arr,n,key)

    return firstOccurrence,lastOccurrence

class TestFirstOccurrence(unittest.TestCase):
    def test_case1(self):
        self.assertEqual((1,3), findFirstAndLastOccurrence([1, 2, 2,2,3, 5], 6, 2))

    def test_no_match(self):
        self.assertEqual((-1,-1), findFirstAndLastOccurrence([1, 3, 4, 24],4, 5))

    def test_case2(self):
        self.assertEqual((1,3), findFirstAndLastOccurrence([1, 7,7,7,8,9,10,11], 8, 7))

    def test_case3(self):
        self.assertEqual((2,3), findFirstAndLastOccurrence([1, 3, 7,7,8,9,10,11], 8,7))

    def test_case4(self):
        self.assertEqual((5,7),findFirstAndLastOccurrence([1,2,3,4,5,6,6,6,7],9,6))


