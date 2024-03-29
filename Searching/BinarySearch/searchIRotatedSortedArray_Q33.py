"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
import unittest
from typing import List

"""
here the approach is:
the problem here is to search for the target in which of the two sorted arrays i the given input:
1. find the pivot index 
2. check if target lies in nums[pivot:] then perform binary search i that array
3. else binary search for target in nums[:pivot]
"""


class Solution:
    def find_pivot(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        mid = s + int((e - s) / 2)

        while s < e:
            if nums[mid] >= nums[0]:
                s = mid + 1
            else:
                e = mid
            mid = s + int((e - s) / 2)
        return s

    def binary_search_target(self, nums: List[int], target: int, low: int, high: int) -> int:
        s = low
        e = high
        mid = s + int((e - s) / 2)

        while s <= e:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
            mid = s + int((e - s) / 2)

        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        if nums[pivot] <= target <= nums[len(nums) - 1]:
            return self.binary_search_target(nums, target, pivot, len(nums) - 1)
        else:
            return self.binary_search_target(nums, target, 0, pivot - 1)


    # one pass for binary search approach:
    """
    Here are the detailed breakdowns of the algorithm:

    1. Initiate the pointer start to 0, and the pointer end to n - 1.

    2. Perform standard binary search. While start <= end:

        i) Take an index in the middle mid as a pivot.

        ii) If nums[mid] == target, the job is done, return mid.

        iii) Now there could be two situations:

            a) Pivot element is larger than the first element in the array, i.e. the subarray from the first element to the pivot is non-rotated, as shown in the following graph.

                - If the target is located in the non-rotated subarray:
                    go left: `end = mid - 1`.

                - Otherwise: go right: `start = mid + 1`.
            b) Pivot element is smaller than the first element of the array, i.e. the rotation index is somewhere between 0 and mid. It implies that the sub-array from the pivot element to the last one is non-rotated, as shown in the following graph.

                - If the target is located in the non-rotated subarray:
                    go right: `start = mid + 1`.

                - Otherwise: go left: `end = mid - 1`.
    3. We're here because the target is not found. Return -1.
    """

    def search_one_pass(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.search([4,5,6,7,0,1,2],0),4)

    def test_case2(self):
        self.assertEqual(self.obj.search([4,5,6,7,0,1,2],3),-1)

    def test_case3(self):
        self.assertEqual(self.obj.search([1],0),-1)

    def test_case1_approach2(self):
        self.assertEqual(self.obj.search_one_pass([4,5,6,7,0,1,2],0),4)

    def test_case2_approach2(self):
        self.assertEqual(self.obj.search_one_pass([4,5,6,7,0,1,2],3),-1)

    def test_case3_approach2(self):
        self.assertEqual(self.obj.search_one_pass([1],0),-1)
