"""
You have n coins, and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:

1 <= n <= 231 - 1

APPROACHES:
Approach 1: Binary Search
This question is easy in a sense that one could run an exhaustive iteration to obtain the result. That could work, except that it would run out of time when the input becomes too large. So let us take a step back to look at the problem, before rushing to the implementation.

Assume that the answer is kk, i.e. we've managed to complete kk rows of coins. These completed rows contain in total 1 + 2 + ... + k = \frac{k (k + 1)}{2}1+2+...+k=
2
k(k+1)
  coins.

We could now reformulate the problem as follows:

Find the maximum k such that \frac{k (k + 1)}{2} \le N
2
k(k+1)
 ≤N.

The problem seems to be one of those search problems. And instead of naive iteration, one could resort to another more efficient algorithm called binary search, as we can find in another similar problem called search insert position.

Complexity Analysis

Time complexity : O(logN).

Space complexity : O(1).

Approach 2:
If we look deeper into the formula of the problem, we could actually solve it with the help of mathematics, without using any iteration.

As a reminder, the constraint of the problem can be expressed as follows:
k(k+1)≤2N

Complexity Analysis

Time complexity :O(1).

Space complexity :O(1).
"""
import unittest

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(((2*n) + 0.25)**0.5 - 0.5)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.arrangeCoins(8),3)

    def test_case2(self):
        self.assertEqual(self.obj.arrangeCoins(5),2)




