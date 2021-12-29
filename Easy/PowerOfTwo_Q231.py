"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false



Constraints:

    -231 <= n <= 231 - 1


Follow up: Could you solve it without loops/recursion?
"""
import unittest


class Solution:
    def isPowerOfTwo_approach_one(self, n: int) -> bool:
        for i in range(0,31):
            num = 2 ** i
            if num == n:
                return True
        return False

    def isPowerOfTwo_approach_two(self, n:int) -> bool:
        num = n
        while num != 0:
            if num == 1:
                return True
            elif num % 2:
                return False
            else:
                num = num / 2
        if num == 0:
            return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case_one_approach_one(self):
        self.assertTrue(self.obj.isPowerOfTwo_approach_one(1))

    def test_case_one_approach_two(self):
        self.assertTrue(self.obj.isPowerOfTwo_approach_two(1))

    def test_case_two_approach_one(self):
        self.assertTrue(self.obj.isPowerOfTwo_approach_one(16))

    def test_case_two_approach_two(self):
        self.assertTrue(self.obj.isPowerOfTwo_approach_two(16))

    def test_case_three_approach_one(self):
        self.assertFalse(self.obj.isPowerOfTwo_approach_one(7))

    def test_case_three_approach_two(self):
        self.assertFalse(self.obj.isPowerOfTwo_approach_two(7))


        