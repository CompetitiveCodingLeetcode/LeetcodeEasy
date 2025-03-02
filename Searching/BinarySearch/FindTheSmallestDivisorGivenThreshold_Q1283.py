"""
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.



Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
Example 2:

Input: nums = [44,22,33,11,1], threshold = 5
Output: 44


Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 106
nums.length <= threshold <= 106
"""
import unittest
from typing import List

class Solution:
    def is_greater(self, nums, temp_min, temp_threshold, threshold):
        greater = False
        for num in nums:
            d = num % temp_min
            if d > 0:
                temp_threshold += (num // temp_min) + 1
            elif d == 0:
                temp_threshold += (num // temp_min)
            if temp_threshold > threshold:
                greater = True
                break
        return greater

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_val = max(nums)
        min_divisor = max_val + 1
        beg = 1
        end = max_val
        mid = (beg + end) // 2
        while beg <= end:
            temp_min = mid
            temp_threshold = 0
            greater = self.is_greater(nums, temp_min, temp_threshold, threshold)
            if greater:
                beg = mid + 1
            else:
                if temp_min < min_divisor:
                    min_divisor = temp_min
                end = mid - 1
            mid = (beg + end) // 2

        return min_divisor

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case_1(self):
        self.assertEqual(self.obj.smallestDivisor([1,2,5,9],6),5)

    def test_case_2(self):
        self.assertEqual(self.obj.smallestDivisor([44,22,33,11,1],5),44)