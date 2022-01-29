"""
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].



Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1


Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.


Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?
"""
import unittest
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        low = 0
        high = len(arr) - 1
        mid = low + int((high - low) / 2)

        while low <= high:
            if arr[mid + 1] < arr[mid] and arr[mid - 1] < arr[mid]:
                return mid
            elif arr[mid + 1] > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = low + int((high - low) / 2)

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj=Solution()

    def test_case1(self):
        self.assertEqual(self.obj.peakIndexInMountainArray([0,1,0]),1)

    def test_case2(self):
        self.assertEqual(self.obj.peakIndexInMountainArray([0,2,1,0]),1)

    def test_case3(self):
        self.assertEqual(self.obj.peakIndexInMountainArray([0,2,3,5,10,8]),4)
