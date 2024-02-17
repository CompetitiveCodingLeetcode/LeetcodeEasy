"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
import unittest


class Solution:
    # recursive solution gives TLE error on leetcode

    def climbStairsDP_bottom_up_space_optimized(self,n):
        if n<0:
            return 0
        if n==0 or n==1:
            return 1
        prev1 = 1
        prev2 = 1
        curr=-1

        for i in range(2,n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return curr

    def climbStairsDP_bottom_up(self,n):
        if n<0:
            return 0
        if n==0:
            return 1
        dp = []
        dp.append(1)
        dp.append(1)

        for i in range(2,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]

    def climbStairsDP_top_down(self,n,dp_arr):
        if n<0:
            return 0
        if n==0:
            return 1
        if dp_arr[n] != -1:
            return dp_arr[n]
        dp_arr[n] = self.climbStairsDP_top_down(n-1,dp_arr) + self.climbStairsDP_top_down(n-2,dp_arr)
        return dp_arr[n]

    def climbStairs(self, n: int) -> int:
        dp_arr = [-1] * (n+1)
        return self.climbStairsDP_top_down(n,dp_arr)

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case_1(self):
        self.assertEqual(self.obj.climbStairs(2),2)

    def test_case_2(self):
        self.assertEqual(self.obj.climbStairs(3),3)

    def test_case_3(self):
        self.assertEqual(self.obj.climbStairsDP_bottom_up(2),2)

    def test_case_4(self):
        self.assertEqual(self.obj.climbStairsDP_bottom_up(3),3)

    def test_case_5(self):
        self.assertEqual(self.obj.climbStairsDP_bottom_up_space_optimized(2),2)

    def test_case_6(self):
        self.assertEqual(self.obj.climbStairsDP_bottom_up_space_optimized(3),3)
