"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.



Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


Constraints:

0 <= x <= 231 - 1
"""
import unittest
from math import e, log


class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        mid = low + int((high - low)/2)
        ans = 0
        if x==0 or x==1:
            return x
        while low<=high:
            if (mid*mid) == x:
                return mid
            elif (mid*mid) > x:
                high = mid -1
            else:
                ans= mid
                low = mid+1
            mid = low + int((high - low)/2)
        return ans


    #O(1) approach to find sqrt
    """
        Before going to the serious stuff, let's first have some fun and implement the algorithm used by the pocket calculators.

        Usually a pocket calculator computes well exponential functions and natural logarithms by having logarithm tables hardcoded or by the other means. Hence the idea is to reduce the square root computation to these two algorithms as well
        sqrt(x) = e**(0.5 * log(x))
        
    """

    def mySqrt_approach2(self, x):
        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.mySqrt(6),2)

    def test_case2(self):
        self.assertEqual(self.obj.mySqrt(0),0)

    def test_case3(self):
        self.assertEqual(self.obj.mySqrt(1),1)

    def test_case4(self):
        self.assertEqual(self.obj.mySqrt(64),8)

    def test_case1_approach2(self):
        self.assertEqual(self.obj.mySqrt_approach2(6),2)

    def test_case2_approach2(self):
        self.assertEqual(self.obj.mySqrt_approach2(0),0)

    def test_case3_approach2(self):
        self.assertEqual(self.obj.mySqrt_approach2(1),1)

    def test_case4_approach2(self):
        self.assertEqual(self.obj.mySqrt_approach2(64),8)