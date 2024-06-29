"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Constraints:

1 <= n <= 104

"""

import sys


class Solution:
    def solve(self, n):
        if n == 0:
            return 0

        ans = n
        i = 1
        while (i * i) <= n:
            ans = min(ans, 1 + self.solve(n - (i * i)))
            i += 1
        return ans

    def solveMem(self, n, square_store):
        if n == 0:
            return 0
        if square_store[n] != -1:
            return square_store[n]
        ans = n
        i = 1
        while (i * i) <= n:
            ans = min(ans, 1 + self.solveMem(n - (i * i), square_store))
            i += 1
        square_store[n] = ans
        return square_store[n]

    def solveTab(self, n):
        square_store = [sys.maxsize] * (n + 1)
        square_store[0] = 0

        for j in range(1, n + 1):
            i = 1
            ans = n
            while (i * i) <= n:
                if n - (i * i) >= 0:
                    square_store[j] = min(square_store[j], 1 + square_store[j - (i * i)])
                i += 1
        return square_store[n]

    def numSquares(self, n: int) -> int:
        # return self.solve(n)

        # square_store = [-1]*(n+1)
        # return self.solveMem(n,square_store)

        return self.solveTab(n)


