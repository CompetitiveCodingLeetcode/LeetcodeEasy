"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""
import unittest
from typing import List


class Solution:
    def moveZeroes_approach1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for num in nums:
            if num != 0:
                nums[counter] = num
                counter += 1

        while counter != len(nums):
            nums[counter] = 0
            counter += 1

        return nums

    #optimized approach
    def moveZeroes_approach2(self,nums: List[int]) -> None:
        counter =0
        for idx,num in enumerate(nums):
            if num != 0:
                temp = nums[counter]
                nums[counter] = nums[idx]
                nums[idx] = temp
                counter += 1

        return nums


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1_approach1(self):
        self.assertListEqual(self.obj.moveZeroes_approach1([0,1,0,3,12]),[1,3,12,0,0])

    def test_case2_approach1(self):
        self.assertListEqual(self.obj.moveZeroes_approach1([0]),[0])

    def test_case1_approach2(self):
        self.assertListEqual(self.obj.moveZeroes_approach2([0,1,0,3,12]),[1,3,12,0,0])

    def test_case2_approach2(self):
        self.assertListEqual(self.obj.moveZeroes_approach2([0]),[0])