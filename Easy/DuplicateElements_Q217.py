"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true



Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109

******IMPORTANT LINK*********
https://leetcode.com/problems/contains-duplicate/solution/
Read the approaches well--- hidden concepts and application how to think for complexity and arrive at best approach
****************************

"""
import unittest
from typing import List

class Solution:

    # this approach gives time limit exceed because of using list as the visited elements data structure...select a data structure which has less time complexity for insert and search operations
    def containsDuplicate_approach1(self, nums: List[int]) -> bool:
        visited = []

        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            else:
                visited.append(nums[i])
        return False


    def containsDuplicate_accepted_approach(self, nums: List[int]) -> bool:
        visited = {}

        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            else:
                visited[nums[i]] = 1
        return False

    def containsDuplicate_using_set(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(set(nums)) < len(nums) else False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj=Solution()

    def test_containsDuplicate_approach1_true(self):
        self.assertTrue(self.obj.containsDuplicate_approach1([1,2,3,1]))

    def test_containsDuplicate_approach1_false(self):
        self.assertFalse(self.obj.containsDuplicate_approach1([1,2,3,4]))

    def test_containsDuplicate_accepted_approach_true(self):
        self.assertTrue(self.obj.containsDuplicate_accepted_approach([1, 2, 3, 1]))

    def test_containsDuplicate_accepted_approach_false(self):
        self.assertFalse(self.obj.containsDuplicate_accepted_approach([1, 2, 3, 4]))

    def test_containsDuplicate_using_set(self):
        self.assertTrue(self.obj.containsDuplicate_using_set([1, 2, 3, 1]))

    def test_containsDuplicate_using_set(self):
        self.assertFalse(self.obj.containsDuplicate_using_set([1, 2, 3, 4]))