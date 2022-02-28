"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).



Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1


Constraints:

1 <= nums.length <= 1000
-100 <= nums[i] <= 100
"""
import unittest
from typing import List


class Solution:
    # time complexity: O(n)
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            count_n = 0
            for num in nums:
                if num < 0:
                    count_n += 1
            if count_n % 2 == 0:
                return 1
            else:
                return -1

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.arraySign([-1,-2,-3,-4,3,2,1]),1)

    def test_case2(self):
        self.assertEqual(self.obj.arraySign([1,5,0,2,-3]),0)

    def test_case3(self):
        self.assertEqual(self.obj.arraySign([-1,1,-1,1,-1]),-1)