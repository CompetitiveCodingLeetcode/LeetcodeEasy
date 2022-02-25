"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0


Constraints:

0 <= n <= 104


Follow up: Could you write a solution that works in logarithmic time complexity?
"""
import unittest


class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_of_zeros = 0
        div = 5
        while div <= n:
            num_of_zeros += n//div
            div *= 5
        return num_of_zeros

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.trailingZeroes(3),0)

    def test_case2(self):
        self.assertEqual(self.obj.trailingZeroes(5),1)

    def test_case3(self):
        self.assertEqual(self.obj.trailingZeroes(0),0)

    def test_case4(self):
        self.assertEqual(self.obj.trailingZeroes(9247),2307)