"""

The TwoSum ques in leetcode assumes only one possible solution
Here assume that you have to return all pairs whose sum is target
"""
import time
from typing import List



# Complexity: Time---O(n^2)  Space-----O(n)
def TwoSumExtension(nums: List[int], target: int) -> List[List[int]]:
    ans_list = []
    start = time.time()
    for i in range(0, len(nums)):
        # if [0,6] and [6,0] both are to be included then j should start from 0 to len of array if only one to be given then start j fro i+1
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                ans_list.append(list((i, j)))
    end = time.time()
    print("time tken by brute force approach=", end - start)
    return ans_list


def find_diff(arr, diff):
    low = 0
    idx = -1
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid][1] < diff:
            low = mid + 1
        elif arr[mid][1] > diff:
            high = mid - 1
        else:
            return arr[mid][0]
    return idx


def sort_key(element):
    return element[1]


# Complexity: Time---O(nlogn)  Space-----O(n)
def TwoSumExtensionApproach2(nums: List[int], target: int) -> List[List[int]]:
    ans_list = []
    temp_num_list = []

    start = time.time()
    for i in range(0, len(nums)):
        temp_num_list.append((i, nums[i]))
    temp_num_list.sort(key=sort_key)

    for i in range(len(nums) - 1):
        diff = target - temp_num_list[i][1]
        idx = find_diff(temp_num_list[i + 1:], diff)
        if idx != -1:
            ans_list.append([temp_num_list[i][0], idx])
    end = time.time()
    print("time taken by optimized approach=", end - start)
    return ans_list


print(TwoSumExtensionApproach2([1, 2, 3, 2, 3, 4, 5, 6], 6))
print(TwoSumExtensionApproach2([2,-3,3,3,-2],0))
print(TwoSumExtension([1, 2, 3, 2, 3, 4, 5, 6], 6))
# Complexity: Time---O(n^2)  Space-----O(n)
