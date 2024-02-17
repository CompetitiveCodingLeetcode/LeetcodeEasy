"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
from typing import List

class Solution:
    # TLE error on leetcode
    def solve_recursively(self,cost,n):
        #base case
        if n==0:
            return cost[0]
        if n==1:
            return cost[1]
        return cost[n] + min(self.solve_recursively(cost,n-1),self.solve_recursively(cost,n-2))

    def solve_top_down_approach(self,cost,n,dp_arr):
        #base case
        if n==0:
            return cost[0]
        if n==1:
            return cost[1]

        if dp_arr[n] != -1:
            return dp_arr[n]

        dp_arr[n] = cost[n] + min(self.solve_top_down_approach(cost,n-1,dp_arr),self.solve_top_down_approach(cost,n-2,dp_arr))
        return dp_arr[n]

    def solve_bottom_up_approach(self,cost,n):
        dp_arr = []
        dp_arr.append(cost[0])
        dp_arr.append(cost[1])

        for i in range(2,n+1):
            dp_arr.append(cost[i]+min(dp_arr[i-1],dp_arr[i-2]))
        return dp_arr[n]

    def solve_bottom_up_space_optimized(self,cost,n):
        prev1 = cost[0]
        prev2 = cost[1]
        curr = -1
        if n==0:
            return prev1
        if n==1:
            return prev2

        for i in range(2,n+1):
            curr = cost[i] + min(prev1,prev2)
            prev1 = prev2
            prev2 = curr
        return curr

    def minCostClimbingStairs(self, cost: List[int],option: int) -> int:
        n = len(cost)
        if option==1:
            return min(self.solve_recursively(cost,n-1),self.solve_recursively(cost,n-2))
        elif option==2:
            dp_arr = [-1]*(n+1)
            return min(self.solve_top_down_approach(cost,n-1,dp_arr),self.solve_top_down_approach(cost,n-2,dp_arr))
        elif option==3:
            return min(self.solve_bottom_up_approach(cost,n-1),self.solve_bottom_up_approach(cost,n-2))
        elif option==4:
            return min(self.solve_bottom_up_space_optimized(cost,n-1),self.solve_bottom_up_space_optimized(cost,n-2))
