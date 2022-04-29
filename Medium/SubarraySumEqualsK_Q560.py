"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
import unittest
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = []
        cumulative_sum.append(0)
        sum_freq = {}
        sum_freq[0] = 1
        latest_sum = cumulative_sum[-1]
        count = 0

        for num in nums:
            latest_sum += num
            cumulative_sum.append(latest_sum)

            if latest_sum - k in sum_freq.keys():
                count += sum_freq[latest_sum - k]
            if latest_sum in sum_freq.keys():
                sum_freq[latest_sum] += 1
            else:
                sum_freq[latest_sum] = 1

        return count


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.subarraySum([1,1,1],2),2)

    def test_case2(self):
        self.assertEqual(self.obj.subarraySum([1,2,3],3),2)

    def test_case3(self):
        self.assertEqual(self.obj.subarraySum([3,9,-2,4,1,-7,2,6,-5,8,-3,-7,6,2,1],5),7)