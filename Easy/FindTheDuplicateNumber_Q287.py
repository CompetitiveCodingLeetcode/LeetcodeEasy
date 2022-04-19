"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""
import unittest
from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num in nums_dict.keys():
                return num
            else:
                nums_dict[num] = 1


    def find_duplicate_optimized_approach(self, nums: List[int]) -> int:



class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.findDuplicate([1,3,4,2,2]),2)

    def test_case2(self):
        self.assertEqual(self.obj.findDuplicate([3,1,3,4,2]),3)

    def test_case3(self):
        self.assertEqual(self.obj.findDuplicate([2,2,2,2,2]),2)