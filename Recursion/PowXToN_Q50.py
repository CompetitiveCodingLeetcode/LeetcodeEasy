"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104


3^11 -- 243*243*3 = 177147
3^5-- 243
3^2 -- 9
3^1 -- 3
"""
import unittest


class Solution:
    def find_pow(self, a, b):
        if b == 0:
            return 1
        if b == 1:
            return a
        ans = self.find_pow(a, b // 2)

        if b % 2 == 0:
            return ans * ans
        else:
            return a * ans * ans

    def myPow(self, x: float, n: int) -> float:
        is_negative = 0
        if n < 0:
            is_negative = 1

        if is_negative:
            ans = self.find_pow(x, -1 * n)
        else:
            ans = self.find_pow(x, n)

        if is_negative:
            return 1 / ans
        else:
            return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case_1(self):
        self.assertEqual(self.obj.myPow(2,0),1)

    def test_case_2(self):
        self.assertEqual(self.obj.myPow(7,1),7)

    def test_case_3(self):
        self.assertEqual(self.obj.myPow(2,-2),0.25)

    def test_case_4(self):
        self.assertEqual(self.obj.myPow(3,11),177147)