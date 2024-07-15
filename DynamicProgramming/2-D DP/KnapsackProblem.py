"""
Problem statement
A thief is robbing a store and can carry a maximal weight of W into his knapsack. There are N items and the ith item weighs wi and is of value vi. Considering the constraints of the maximum weight that a knapsack can carry, you have to find and return the maximum value that a thief can generate by stealing items.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= N <= 10^2
1<= wi <= 50
1 <= vi <= 10^2
1 <= W <= 10^3

Time Limit: 1 second
Sample Input:
1
4
1 2 4 5
5 4 8 6
5
Sample Output:
13
"""

from os import *
from sys import *
from collections import *
from math import *


## Read input as specified in the question.
## Print output as specified in the question.

# User function Template for python3

class Solution:
    def solve(self, W, wt, val, n, index):
        if index == 0:
            if wt[0] <= W:
                return val[0]
            else:
                return 0

        include = 0
        if wt[index] <= W:
            include = val[index] + self.solve(W - wt[index], wt, val, n, index - 1)

        exclude = 0 + self.solve(W, wt, val, n, index - 1, ans)

        return max(include, exclude)

    def solveMem(self, W, wt, val, n, index, ans_store):
        if index == 0:
            if wt[0] <= W:
                return val[0]
            else:
                return 0

        if ans_store[index][W] != -1:
            return ans_store[index][W]

        include = 0
        if wt[index] <= W:
            include = val[index] + self.solveMem(W - wt[index], wt, val, n, index - 1, ans_store)
        exclude = 0 + self.solveMem(W, wt, val, n, index - 1, ans_store)

        ans_store[index][W] = max(include, exclude)
        return ans_store[index][W]

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):

        # code here
        # index = n-1
        # ans = self.solve(W,wt,val,n,index)

        # memoization
        index = n - 1
        ans_store = []
        for i in range(0, n):
            temp = []
            for j in range(0, W + 1):
                temp.append(-1)
            ans_store.append(temp)

        ans = self.solveMem(W, wt, val, n, index, ans_store)

        return ans


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        wt = list(map(int, input().strip().split()))
        val = list(map(int, input().strip().split()))
        W = int(input())
        ob = Solution()
        print(ob.knapSack(W, wt, val, n))