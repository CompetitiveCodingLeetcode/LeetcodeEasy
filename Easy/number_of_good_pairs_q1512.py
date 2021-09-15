""""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0



Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 100


"""
import unittest
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

    def numIdenticalPairsOnePass(self, nums: List[int]) -> int:
        count_num = {}
        count = 0
        for num in nums:
            if num in count_num:
                count_num[num] += 1
            else:
                count_num[num] = 1

        for item in count_num.keys():
            if count_num[item] > 1:
                count += (count_num[item]*(count_num[item] - 1))/2

        return count
        

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj=Solution()

    def test_numIdenticalPairs1(self):
        self.assertEqual(self.obj.numIdenticalPairs([1,2,3,1]),1)

    def test_numIdenticalPairs2(self):
        self.assertEqual(self.obj.numIdenticalPairs([1,2,3,4]),0)

    def test_numIdenticalPairs3(self):
        self.assertEqual(self.obj.numIdenticalPairs([1,2,3,1,1,3]),4)

    def test_numIdenticalPairs4(self):
        self.assertEqual(self.obj.numIdenticalPairs([1,1,1,1]),6)

    def test_numIdenticalPairsOnePass1(self):
        self.assertEqual(self.obj.numIdenticalPairsOnePass([1,2,3,1]),1)

    def test_numIdenticalPairsOnePass2(self):
        self.assertEqual(self.obj.numIdenticalPairsOnePass([1,2,3,4]),0)

    def test_numIdenticalPairsOnePass3(self):
        self.assertEqual(self.obj.numIdenticalPairsOnePass([1,2,3,1,1,3]),4)

    def test_numIdenticalPairsOnePass4(self):
        self.assertEqual(self.obj.numIdenticalPairsOnePass([1,1,1,1]),6)
