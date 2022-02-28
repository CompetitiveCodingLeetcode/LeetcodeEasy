"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
import unittest
from typing import List


class Solution:
    # time complexity: O(len(nums1)) ; space complexity: O(n)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        is_nums1 = False
        nums = []

        if nums1_len < nums2_len:
            nums = nums1
            is_nums1 = True
        else:
            nums = nums2

        for num in nums:
            if is_nums1:
                if num in nums2 and num not in ans:
                    ans.append(num)
            else:
                if num in nums1 and num not in ans:
                    ans.append(num)

        return ans

    def intersection_optimized_approach(self,nums1,nums2):
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set & nums2_set)


class TestSoluton(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.intersection([1,2,2,1],[2,2]),[2])
        self.assertListEqual(self.obj.intersection_optimized_approach([1, 2, 2, 1], [2, 2]), [2])

    def test_case2(self):
        self.assertListEqual(self.obj.intersection([4,9,5],[9,4,9,8,4]),[4,9])
        self.assertListEqual(self.obj.intersection_optimized_approach([4, 9, 5], [9, 4, 9, 8, 4]), [9, 4])
