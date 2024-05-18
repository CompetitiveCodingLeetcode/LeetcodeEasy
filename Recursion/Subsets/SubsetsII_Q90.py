"""
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

from typing import List

class Solution:
    def solve(self, nums, idx, data, ans):
        if idx >= len(nums):
            data = sorted(data)
            if data not in ans:
                ans.append(data.copy())
            return

        # exclude call
        self.solve(nums, idx + 1, data, ans)

        # include call
        data.append(nums[idx])
        self.solve(nums, idx + 1, data, ans)
        data.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        data = []
        idx = 0
        self.solve(nums, idx, data, ans)
        return ans