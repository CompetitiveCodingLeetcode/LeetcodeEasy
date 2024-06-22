"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400


Approach is based on inclusion and exclusion. if included current val then what should be the next value. If excluded then what should be the next value.

Variant of max sum of non-adjacent elements
"""
from typing import List

class Solution:
    #recursive + memoization solution
    def solve(self, nums, idx, store_res):
        if idx < 0:
            return 0
        elif idx == 0:
            return nums[0]

        if store_res[idx] != -1:
            return store_res[idx]

        incl = self.solve(nums, idx - 2, store_res) + nums[idx]
        excl = self.solve(nums, idx - 1, store_res)

        store_res[idx] = max(incl, excl)
        return store_res[idx]

    def solve_tab(self, nums):

        prev2 = 0
        prev1 = nums[0]

        for i in range(1, len(nums)):
            incl = prev2 + nums[i]
            excl = prev1
            ans = max(incl, excl)
            prev2 = prev1
            prev1 = ans
        return prev1

    def rob(self, nums: List[int]) -> int:
        idx = len(nums)
        store_res = [-1] * idx
        ans_rec = self.solve(nums,idx-1,store_res)
        ans = self.solve_tab(nums)
        return ans

# example test cases:
# [1,2] ans = 2
# [2,3,2] ans= 4
