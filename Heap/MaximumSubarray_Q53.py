"""
Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

getting TLE on leetcode
"""
import unittest
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_arr = []
        k = 1
        for i in range(0, len(nums)):
            subset_sum = 0
            for j in range(i, len(nums)):
                subset_sum += nums[j]
                if len(sum_arr) < k:
                    heappush(sum_arr, subset_sum)
                elif subset_sum > sum_arr[0]:
                    heappop(sum_arr)
                    heappush(sum_arr, subset_sum)

        return sum_arr[-1]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case_1(self):
        self.assertEqual(self.obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]),6)

    def test_case_2(self):
        self.assertEqual(self.obj.maxSubArray([1]),1)

    def test_case_3(self):
        self.assertEqual(self.obj.maxSubArray([5,4,-1,7,8]),23)