"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:
Input: heights = [2,4]
Output: 4


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

APPROACH: it follows the approach of previous and next smallest element.
- find prev smaller element indices for each height(p)
- find next smaller element indices for each height(n)
- here , the length ie., height at a particular index is fixed and breadth is varying.
    breadth = n-p-1
    however, for cases like test_case3 : where n= -1, in that case n = len(heights)
- find current area, if this is greater than max_area then max_area = current area.
"""
import unittest
from typing import List


class Solution:
    def find_next_smaller_heights(self, nums):
        ans = [-1] * len(nums)
        stack = [-1]

        for i in range(len(nums) - 1, -1, -1):
            if stack[-1] != -1 and nums[stack[-1]] >= nums[i]:
                while stack[-1] != -1 and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                ans[i] = stack[-1]
                stack.append(i)

            else:
                ans[i] = stack[-1]
                stack.append(i)

        return ans

    def find_prev_smaller_heights(self, nums):
        elements = [-1]
        ans = [-1] * len(nums)
        for i in range(0, len(nums)):
            if elements[-1] != -1 and nums[elements[-1]] >= nums[i]:
                while elements[-1] != -1 and nums[elements[-1]] >= nums[i]:
                    elements.pop()
                ans[i] = elements[-1]
                elements.append(i)
            else:
                ans[i] = elements[-1]
                elements.append(i)

        return ans

    # time complexity: O(n), space complexity: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        next_smaller_heights = self.find_next_smaller_heights(heights)
        prev_smaller_heights = self.find_prev_smaller_heights(heights)
        l, b = 0, 0
        max_area = 0
        area = 0
        for i in range(0, len(heights)):
            l = heights[i]
            if next_smaller_heights[i] == -1:
                next_smaller_heights[i] = len(heights)
            b = next_smaller_heights[i] - prev_smaller_heights[i] - 1
            area = l * b
            if area > max_area:
                max_area = area
        return max_area

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.largestRectangleArea([2,1,5,6,2,3]),10)

    def test_case2(self):
        self.assertEqual(self.obj.largestRectangleArea([2,4]),4)

    def test_case3(self):
        self.assertEqual(self.obj.largestRectangleArea([2,2,2,2]),8)

