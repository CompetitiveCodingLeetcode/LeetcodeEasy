"""
in an array [3,4,5,6,1] , pivot is the index at which min element in array occurs.
fid min in roatated sorted array is a variant of this
"""
import unittest
from typing import List


class Solution:
    def find_pivot(self,nums: List[int]) -> int:
        s = 0
        e = len(nums) -1
        mid = s + int((e-s)/2)
        while s< e:
            if nums[mid] >= nums[0]:
                s = mid+1
            else:
                e = mid
            mid = s + int((e-s)/2)
        return s

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.find_pivot([6,7,1,2,3]),2)

    def test_case2(self):
        self.assertEqual(self.obj.find_pivot([6,7,8,1,2]),3)

    def test_case3(self):
        self.assertEqual(self.obj.find_pivot([7,1,2,3,4]),1)