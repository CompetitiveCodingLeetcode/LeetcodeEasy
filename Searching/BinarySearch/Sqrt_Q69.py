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