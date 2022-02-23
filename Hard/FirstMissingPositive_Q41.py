"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution:
    def remove_negative_nums(self,A):
        temp = []
        for num in A:
            if num > 0:
                temp.append(num)
        return temp
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        num_of_negative_int = 0
        for num in nums:
            if num<=0:
                num_of_negative_int += 1
        if n == num_of_negative_int:
            return 1
        else:
            temp =[]
            temp = self.remove_negative_nums(nums)
            min_num = min(temp)
            if min_num != 1:
                return 1
            else:
                # temp = sorted(temp)
                for i in range(1,len(temp)):
                    if min_num+1 in temp:
                        min_num += 1
                    else:
                        return min_num + 1
                return min_num + 1