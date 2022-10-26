"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6


"""
import unittest
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        i = 0
        for num in nums:
            prefix_sum += nums[i]
            nums[i] = prefix_sum
            i += 1
        return nums

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.runningSum([1,2,3,4]),[1,3,6,10])

    def test_case2(self):
        self.assertEqual(self.obj.runningSum([1,1,1,1,1]),[1,2,3,4,5])

    def test_case3(self):
        self.assertEqual(self.obj.runningSum([3,1,2,10,1]),[3,4,6,16,17])