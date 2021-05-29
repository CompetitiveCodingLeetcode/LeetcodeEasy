"""

The TwoSum ques in leetcode assumes only one possible solution
Here assume that you have to return all pairs whose sum is target
"""
from typing import List


def TwoSumExtension(nums: List[int], target: int) -> List[List[int]]:
    ans_list = []
    for i in range(0, len(nums)):
        # if [0,6] and [6,0] both are to be included then j should start from 0 to len of array if only one to be given then start j fro i+1
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target and nums[i] != nums[j]:
                ans_list.append(list((i, j)))

    return ans_list


print(TwoSumExtension([1, 2, 3, 2, 3, 4, 5, 6], 6))

#Complexity: Time---O(n^2)  Space-----O(n)