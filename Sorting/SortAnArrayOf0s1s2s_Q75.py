"""
An array that contains 0s,1s and 2s
Sort the array
"""
import unittest
from typing import List

class Solution:
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums

    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)-1

        for curr in range(0,len(nums)):
            if nums[curr] == 0:
                nums = self.swap(nums,curr,start)
                start += 1
            elif nums[curr] == 2:
                nums = self.swap(nums,curr,end)
                end -= 1
            if curr == end or start==end:
                break

        return nums

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case_1(self):
        self.assertListEqual(self.obj.sortColors([2,0,2,1,1,0]),[0,0,1,1,2,2])

    def test_case_2(self):
        self.assertListEqual(self.obj.sortColors([2,0,1]),[0,1,2])