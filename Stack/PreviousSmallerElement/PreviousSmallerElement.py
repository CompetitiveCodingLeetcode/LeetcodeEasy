"""
given a list of numbers, find the previous smaller element corresponding to each element in list
"""
import unittest
from typing import List


class Solution():
    def find_prev_smaler_element(self,nums:List[int]):
        elements= [-1]
        ans = [-1]*len(nums)
        for i in range(0,len(nums)):
            if elements[-1] >= nums[i]:
                while elements[-1] >= nums[i]:
                    elements.pop()
                ans[i] = elements[-1]
                elements.append(nums[i])
            else:
                ans[i] = elements[-1]
                elements.append(nums[i])

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.find_prev_smaler_element([4, 8, 5, 2, 25]),[-1,4,4,-1,2])

    def test_case2(self):
        self.assertListEqual(self.obj.find_prev_smaler_element([13, 7, 6, 12]),[-1,-1,-1,6])

    def test_case3(self):
        self.assertListEqual(self.obj.find_prev_smaler_element([11,13,21,3]),[-1,11,13,-1])



