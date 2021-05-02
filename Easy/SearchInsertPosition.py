"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:

Input: nums = [1], target = 0
Output: 0



Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104

"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = -1
        len_nums = len(nums)
        for idx, num in enumerate(nums):
            if num == target:
                index = idx
                break
        if index == -1:
            for idx, num in enumerate(nums):
                if num > target:
                    index = idx
                    break
                elif (num < target) and (idx == len_nums - 1):
                    index = idx + 1
        return index

obj = Solution()
print(obj.searchInsert([1,3,4,7],6))