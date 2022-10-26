"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21


Constraints:

1 <= n <= 10^5
"""
import unittest


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_prod = 1
        n_sum = 0
        temp = n
        while temp != 0:
            d = temp % 10
            n_prod *= d
            n_sum += d
            temp = temp // 10

        return n_prod - n_sum

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.subtractProductAndSum(234),15)

    def test_case2(self):
        self.assertEqual(self.obj.subtractProductAndSum(4421),21)

