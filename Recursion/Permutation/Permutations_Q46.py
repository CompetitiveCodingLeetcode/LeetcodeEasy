"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


APPROACH:
1. if there are n digits then total permutations will be : n!
2. for each place there should be all n digits placements.
for explanation of solution: https://www.youtube.com/watch?v=va3NEycUxsg&list=PLDzeHZWIZsTqBmRGnsCOGNDG5FY0G04Td&index=9
"""
import unittest
from typing import List


class Solution:
    def swap(self, nums: List[int], i: int, j: int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def find_permutations(self, nums: List[int], idx: int, ans: List[List[int]]):
        if idx >= len(nums):
            ans.append(nums.copy())
            return
        else:
            for i in range(idx, len(nums)):
                self.swap(nums, idx, i)
                self.find_permutations(nums, idx + 1, ans)
                # backtracking
                self.swap(nums, idx, i)

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.find_permutations(nums, 0, ans)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def is_present(self,actual_ans,expected_ans)->bool:
        if len(actual_ans) != len(expected_ans):
            return False
        for item in actual_ans:
            if item not in expected_ans:
                return False
        return True

    def test_case1(self):
        actual_ans = self.obj.permute([1,2,3])
        expected_ans = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        ans = self.is_present(actual_ans,expected_ans)
        self.assertTrue(ans)



    def test_case2(self):
        actual_ans=self.obj.permute([0,1])
        expected_ans=[[0,1],[1,0]]
        ans=self.is_present(actual_ans,expected_ans)
        self.assertTrue(ans)

    def test_case3(self):
        actual_ans = self.obj.permute([1])
        expected_ans = [[1]]
        ans=self.is_present(actual_ans,expected_ans)
        self.assertTrue(ans)