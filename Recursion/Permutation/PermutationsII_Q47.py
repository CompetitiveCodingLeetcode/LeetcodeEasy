"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from typing import List

class Solution:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def solve(self, nums, idx, ans):
        if idx >= len(nums):
            if nums not in ans:
                ans.append(nums.copy())
            return

        for i in range(idx, len(nums)):
            self.swap(nums, idx, i)
            self.solve(nums, idx + 1, ans)
            self.swap(nums, idx, i)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        idx = 0
        self.solve(nums, idx, ans)
        return ans

