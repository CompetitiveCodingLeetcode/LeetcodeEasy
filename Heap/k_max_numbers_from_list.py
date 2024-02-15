"""
given a list of numbers, find k largest numbers from the list.
For example,
nums = [-1, -2, 0, 16, 177, -19, 34, 3]
ans = [16,177,34]
"""

from heapq import heapify

def find_k_max_elements(nums,k):
    nums = [(-1*num) for num in nums]
    heapify(nums)
    nums = [(-1*num) for num in nums]
    print(nums[0:k])

find_k_max_elements([-1, -2, 0, 16, 177, -19, 34, 3],3)
