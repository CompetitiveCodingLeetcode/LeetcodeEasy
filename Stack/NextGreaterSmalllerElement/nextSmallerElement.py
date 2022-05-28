"""
given a list of elements, find the next smaller element corresponding to each element in the list.

APPROACH:
- start from the last element and put -1 in the stack
- for the last element the next smaller element in the array is nothing hence -1. and push the current element in stack.
- for each other element of the list ---
    - if stack.top() is smaller than current ellement:
        store current in ans
    - else
        keep popping elemnts from the stack until stack.top() becomes smaller than the current element and then store the ans.
"""
import unittest
from typing import List


class Solution():
    def find_next_smaller_element(self,nums:List[int]):
        ans = [-1]*len(nums)
        stack = [-1]

        for i in range(len(nums)-1,-1,-1):
            if stack[-1] >= nums[i]:
                while stack[-1] >= nums[i]:
                    stack.pop()
                ans[i] = stack[-1]
                stack.append(nums[i])

            else:
                ans[i] = stack[-1]
                stack.append(nums[i])

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.find_next_smaller_element([4, 8, 5, 2, 25]),[2,5,2,-1,-1])

    def test_case2(self):
        self.assertListEqual(self.obj.find_next_smaller_element([13, 7, 6, 12]),[7,6,-1,-1])

    def test_case3(self):
        self.assertListEqual(self.obj.find_next_smaller_element([11,13,21,3]),[3,3,3,-1])
