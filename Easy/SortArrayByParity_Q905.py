"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.



Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""
import unittest
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ptr1 = 0
        ptr2 = len(nums) - 1
        while ptr1 < ptr2:
            if nums[ptr1] % 2 == 0:
                ptr1 += 1
            else:
                if nums[ptr2] % 2 == 0:
                    temp = nums[ptr1]
                    nums[ptr1] = nums[ptr2]
                    nums[ptr2] = temp
                    ptr1 += 1
                    ptr2 -= 1
                else:
                    ptr2 -= 1
        return nums

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.sortArrayByParity([3,1,2,4]),[4,2,1,3])

    def test_case2(self):
        self.assertListEqual(self.obj.sortArrayByParity([0]),[0])