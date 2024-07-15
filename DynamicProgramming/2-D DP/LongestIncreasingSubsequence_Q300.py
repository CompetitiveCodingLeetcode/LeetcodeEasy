"""
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from typing import List

class Solution:
    def solve(self, nums, curr, prev):
        if curr == len(nums):
            return 0
        take = 0
        if (prev == -1) or (nums[curr] > nums[prev]):
            take = 1 + self.solve(nums, curr + 1, curr)
        not_take = 0 + self.solve(nums, curr + 1, prev)
        ans = max(take, not_take)
        return ans

    def solveMem(self, nums, curr, prev, ans_store):
        if curr == len(nums):
            return 0
        if ans_store[curr][prev + 1] != -1:
            return ans_store[curr][prev + 1]

        take = 0
        if (prev == -1) or (nums[curr] > nums[prev]):
            take = 1 + self.solveMem(nums, curr + 1, curr, ans_store)
        not_take = 0 + self.solveMem(nums, curr + 1, prev, ans_store)
        ans_store[curr][prev + 1] = max(take, not_take)
        return ans_store[curr][prev + 1]

    def solveTab(self, nums):
        ans_store = []
        for i in range(0, len(nums) + 1):
            temp = []
            for j in range(0, len(nums) + 1):
                temp.append(0)
            ans_store.append(temp)

        for curr in range(len(nums) - 1, -1, -1):
            for prev in range(curr - 1, -2, -1):
                take = 0
                if (prev == -1) or (nums[curr] > nums[prev]):
                    take = 1 + ans_store[curr + 1][curr + 1]
                not_take = 0 + ans_store[curr + 1][prev + 1]
                ans_store[curr][prev + 1] = max(take, not_take)
        return ans_store[0][0]

    def solveTabSO(self, nums):
        currRow = []
        nxtRow = []
        for i in range(0, len(nums) + 1):
            currRow.append(0)
            nxtRow.append(0)

        for curr in range(len(nums) - 1, -1, -1):
            for prev in range(curr - 1, -2, -1):
                take = 0
                if (prev == -1) or (nums[curr] > nums[prev]):
                    take = 1 + nxtRow[curr + 1]
                not_take = 0 + nxtRow[prev + 1]
                currRow[prev + 1] = max(take, not_take)
            nxtRow = currRow
        return nxtRow[0]

    # 0,2 mid = 1
    # [2,3,7] 4
    # [2,3,5,7]

    def find_lower_bound(self, low, high, val, arr):
        while low <= high:
            mid = low + int((high - low) / 2)
            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans

    def solveTOBinarySearch(self, nums):
        ans = []
        for i in range(0, len(nums)):
            if len(ans) == 0 or nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                idx = self.find_lower_bound(0, len(ans) - 1, nums[i], ans)
                ans[idx] = nums[i]
        return len(ans)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # prev = -1
        # curr = 0
        # ans = self.solve(nums,curr,prev)

        # ans_store = []
        # prev = -1
        # curr = 0
        # for i in range(0,len(nums)):
        #     temp = []
        #     for j in range(0,len(nums)+1):
        #         temp.append(-1)
        #     ans_store.append(temp)
        # ans = self.solveMem(nums,curr,prev,ans_store)

        # ans = self.solveTab(nums)

        # ans = self.solveTabSO(nums)

        ans = self.solveTOBinarySearch(nums)
        return ans
