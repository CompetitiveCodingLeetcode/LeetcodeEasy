"""

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1


Time complexity(using fast and slow pointer):
- since the number of digits in a number n = floor(log n) + 1, hence the coplexity = o(log n)

Space complexity:
O(1)
"""
import unittest


class Solution:
    def sum_of_digits_sqaured(self, n):
        total = 0
        while n != 0:
            digit = n % 10
            n = n // 10
            total += (digit * digit)
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sum_of_digits_sqaured(n)

        while slow != fast and fast != 1:
            slow = self.sum_of_digits_sqaured(slow)
            fast = self.sum_of_digits_sqaured(self.sum_of_digits_sqaured(fast))

        if fast == 1:
            return True
        return False

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.isHappy(19))

    def test_case2(self):
        self.assertFalse(self.obj.isHappy(2))