"""
return True if given array is sorted, else return False.
"""
import unittest
from typing import List


class Solution:
    def isSorted(self,arr : List[int], size: int)-> bool:
        if size == 0 or size == 1:
            return True
        if arr[0] <= arr[1]:
            return self.isSorted(arr[1:],size-1)
        else:
            return False

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.isSorted([1,3,5,7],4))

    def test_case2(self):
        self.assertTrue(self.obj.isSorted([],0))

    def test_case3(self):
        self.assertTrue(self.obj.isSorted([3],1))

    def test_case4(self):
        self.assertFalse(self.obj.isSorted([1,2,3,0],4))

    def test_case5(self):
        self.assertTrue(self.obj.isSorted([1,1,1],3))