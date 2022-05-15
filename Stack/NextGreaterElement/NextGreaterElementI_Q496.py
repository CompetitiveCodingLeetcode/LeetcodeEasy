"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.


Follow up: Could you find an O(nums1.length + nums2.length) solution?

"""
import unittest
from typing import List


class Solution:
    def find_element(self, num, nums):
        count = 0
        for n in nums:
            if n == num:
                return count
            else:
                count += 1

    #time complexity: O(nm^2) where n= len(nums1) and m = len(nums2)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = -1
        ans = []
        flag = 0
        for i in range(0, len(nums1)):
            flag = 0
            idx = self.find_element(nums1[i], nums2)
            for j in range(idx, len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    flag = 1
                    break
            if flag == 0:
                ans.append(-1)
        return ans

    def next_greater_element_optimized(self,nums1,nums2):
        ans = []
        mapping = {}
        stack = []
        for num in nums2:
            if len(stack) == 0:
                stack.append(num)
            else:
                while len(stack) != 0 and num > stack[-1]:
                    mapping[stack.pop()] = num
                stack.append(num)
        while len(stack) != 0:
            mapping[stack.pop()] = -1

        for num in nums1:
            ans.append(mapping[num])

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.nextGreaterElement([4,1,2],[1,3,4,2]),[-1,3,-1])

    def test_case2(self):
        self.assertListEqual(self.obj.nextGreaterElement([2,4],[1,2,3,4]),[3,-1])

    def test_case1_optimized(self):
        self.assertListEqual(self.obj.next_greater_element_optimized([4,1,2],[1,3,4,2]),[-1,3,-1])

    def test_case2_optimized(self):
        self.assertListEqual(self.obj.next_greater_element_optimized([2,4],[1,2,3,4]),[3,-1])

    def test_case3_optimized(self):
        self.assertListEqual(self.obj.next_greater_element_optimized([1,3,4,5,2],[6,5,4,3,2,1,7]),[7,7,7,7,7])
