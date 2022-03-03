"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
import unittest
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = {}
        for num in nums:
            if num in nums_count.keys():
                return True
            else:
                nums_count[num] = 1
        return False

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.containsDuplicate([1,2,3,1]))

    def test_case2(self):
        self.assertFalse(self.obj.containsDuplicate([1,2,3,4]))

    def test_case3(self):
        self.assertTrue(self.obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))