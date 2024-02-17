"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:

0 <= n <= 30
"""
import unittest


class Solution:
    def fib_recursive(self, n: int) -> int:
        if n==0 or n==1:
            return n
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_dp_memoization(self,n,dp_arr):
        if n==0 or n==1:
            return n
        if dp_arr[n] != -1:
            return dp_arr[n]

        dp_arr[n] = self.fib_dp_memoization(n-1,dp_arr) + self.fib_dp_memoization(n-2,dp_arr)
        return dp_arr[n]

    def fib(self, n: int) -> int:
        dp_arr = [-1]*(n+1)
        return self.fib_dp_memoization(n, dp_arr)

    def fib_dp_tabulation(self,n: int) -> int:
        dp = []
        dp.append(0)
        dp.append(1)
        for i in range(2,n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[n]

    def fib_dp_tabulation_space_optimized(self,n: int) -> int:
        if n==0 or n==1:
            return n
        prev1 = 0
        prev2 = 1
        curr=-1
        for i in range(2,n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return curr


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_recursive_1(self):
        self.assertEqual(self.obj.fib_recursive(3),2)

    def test_recursive_2(self):
        self.assertEqual(self.obj.fib_recursive(1),1)

    def test_recursive_3(self):
        self.assertEqual(self.obj.fib_recursive(6),8)

    def test_dp_1(self):
        self.assertEqual(self.obj.fib(3),2)

    def test_dp_2(self):
        self.assertEqual(self.obj.fib_recursive(1),1)

    def test_dp_3(self):
        self.assertEqual(self.obj.fib_recursive(6),8)

    def test_dp_tabulation_1(self):
        self.assertEqual(self.obj.fib_dp_tabulation(3),2)

    def test_dp_tabulation_2(self):
        self.assertEqual(self.obj.fib_dp_tabulation(1),1)

    def test_dp_tabulation_3(self):
        self.assertEqual(self.obj.fib_dp_tabulation(6),8)

    def test_dp_tabulation_space_optimized_1(self):
        self.assertEqual(self.obj.fib_dp_tabulation_space_optimized(3),2)

    def test_dp_tabulation_space_optimized_2(self):
        self.assertEqual(self.obj.fib_dp_tabulation_space_optimized(1),1)

    def test_dp_tabulation_space_optimized_3(self):
        self.assertEqual(self.obj.fib_dp_tabulation_space_optimized(6),8)
