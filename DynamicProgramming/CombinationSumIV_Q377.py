"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000


Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?

"""

from typing import List
class Solution:
    def solve(self, nums, target):
        if target == 0:
            return 1
        if target < 0:
            return 0
        ans = 0
        for i in range(0, len(nums)):
            ans += self.solve(nums, target - nums[i])

        return ans

    def solveMem(self, nums, target, target_store):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target_store[target] != -1:
            return target_store[target]
        ans = 0
        for i in range(0, len(nums)):
            ans += self.solveMem(nums, target - nums[i], target_store)

        target_store[target] = ans
        return target_store[target]

    def solveTab(self, nums, target):
        target_store = [0] * (target + 1)
        target_store[0] = 1
        for i in range(1, target + 1):
            for j in range(0, len(nums)):
                if target - nums[j] >= 0:
                    target_store[i] += target_store[i - nums[j]]

        return target_store[target]

    def combinationSum4(self, nums: List[int], target: int) -> int:
        # ans = self.solve(nums,target)

        # target_store = [-1]*(target+1)
        # ans = self.solveMem(nums,target,target_store)

        ans = self.solveTab(nums, target)
        return ans
