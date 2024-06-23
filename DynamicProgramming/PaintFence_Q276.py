"""
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
There cannot be three or more consecutive posts with the same color.
Given the two integers n and k, return the number of ways you can paint the fence.



Example 1:


Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.
Example 2:

Input: n = 1, k = 1
Output: 1
Example 3:

Input: n = 7, k = 2
Output: 42


Constraints:

1 <= n <= 50
1 <= k <= 105
The testcases are generated such that the answer is in the range [0, 231 - 1] for the given n and k.


APPROACH:
For colouring n posts with no more than 2 posts with same colour using k colours:
1. check 2 cases for n=2 where both posts are coloured same and secondly, both posts are of different colors.
2. Extend n=2 to n=3 and try to link with n=2.
3. Same of n=3 is linked to diff of n=2 and diff of n=3 is linked to total of n=2.
4. Further, extend the logic to n=4 and you’ll get recursive relation
"""


class Solution:
    def solve(self, n, k):
        if n == 1:
            return k
        elif n == 2:
            return (k + (k * (k - 1)))

        ans = (k - 1) * (self.solve(n - 1, k) + self.solve(n - 2, k))
        return ans

    def solveMem(self, n, k, ans_store):
        if n == 1:
            return k
        elif n == 2:
            return (k + (k * (k - 1)))

        if ans_store[n] != -1:
            return ans_store[n]

        ans_store[n] = (k - 1) * (self.solveMem(n - 1, k, ans_store) + self.solveMem(n - 2, k, ans_store))
        return ans_store[n]

    def solveTab(self, n, k):
        ans_store = [-1] * (n + 1)
        if n >= 1:
            ans_store[1] = k
        if n >= 2:
            ans_store[2] = (k + (k * (k - 1)))

        for i in range(3, n + 1):
            ans_store[i] = (k - 1) * (ans_store[i - 1] + ans_store[i - 2])
        return ans_store[n]

    def solveTabSpaceOptimized(self, n, k):
        if n >= 1:
            prev2 = k
        if n >= 2:
            prev1 = (k + (k * (k - 1)))

        for i in range(3, n + 1):
            curr = (k - 1) * (prev1 + prev2)
            prev2 = prev1
            prev1 = curr
        if n == 1:
            return prev2
        return prev1

    def numWays(self, n: int, k: int) -> int:
        # ans = self.solve(n,k)

        # ans_store = [-1]*(n+1)
        # ans = self.solveMem(n,k,ans_store)

        # ans = self.solveTab(n,k)

        ans = self.solveTabSpaceOptimized(n, k)
        return ans
