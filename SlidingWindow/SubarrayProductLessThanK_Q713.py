"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.



Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0


Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""
import unittest
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
            l = 0
            r = 0
            prod = 1
            ans = 0
            for r in range(0,len(nums)):
                prod = prod*nums[r]
                while prod >= k and l <= r:
                    prod = prod/nums[l]
                    l += 1
                ans = ans+(r-l+1)
            return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.numSubarrayProductLessThanK([10,5,2,6],100),8)

    def test_case2(self):
        self.assertEqual(self.obj.numSubarrayProductLessThanK([1,2,3],0),0)