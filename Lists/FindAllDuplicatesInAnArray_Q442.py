"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]

Example 3:

Input: nums = [1]
Output: []



Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n
    Each element in nums appears once or twice.






ex: [10,2,5,10,9,1,1,4,3,7]
"""
import unittest
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for x in nums:
            if nums[abs(x) - 1] >= 0:
                nums[abs(x) - 1] = -1 * nums[abs(x) - 1]
            else:
                duplicates.append(abs(x))

        return duplicates


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case_one(self):
        self.assertListEqual(self.obj.findDuplicates([4,3,2,7,8,2,3,1]),[2,3])

    def test_case_two(self):
        self.assertListEqual(self.obj.findDuplicates([1,1,2]),[1])

    def test_case_three(self):
        self.assertListEqual(self.obj.findDuplicates([1]),[])

    def test_case_four(self):
        self.assertListEqual(self.obj.findDuplicates([10,2,5,10,9,1,1,4,3,7]),[10,1])
