"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
import unittest
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        ans = 0
        cnt_0 = 0
        for i in range(r, len(nums)):
            if nums[i] == 0:
                cnt_0 += 1
            while cnt_0 > 1:
                if nums[l] == 0:
                    cnt_0 -= 1
                l += 1
            ans = max(ans, i - l + 1)
        return ans - 1

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case_1(self):
        self.assertEqual(self.obj.longestSubarray([1,1,0,1]),3)

    def test_case_2(self):
        self.assertEqual(self.obj.longestSubarray([0,1,1,1,0,1,1,0,1]),5)

    def test_case_3(self):
        self.assertEqual(self.obj.longestSubarray([1,1,1]),2)

    def test_case_4(self):
        self.assertEqual(self.obj.longestSubarray([1,1,0,0,1,1,1,0,1]),4)