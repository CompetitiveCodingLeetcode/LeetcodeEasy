"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

"""
APPROACH:
 Two Pointer
Intuition

Since the array A is sorted, loosely speaking it has some negative elements with squares in decreasing order, then some non-negative elements with squares in increasing order.

For example, with [-3, -2, -1, 4, 5, 6], we have the negative part [-3, -2, -1] with squares [9, 4, 1], and the positive part [4, 5, 6] with squares [16, 25, 36]. Our strategy is to iterate over the negative part in reverse, and the positive part in the forward direction.

Algorithm

We can use two pointers to read the positive and negative parts of the array - one pointer j in the positive direction, and another i in the negative direction.

Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together using a two-pointer technique.

Complexity Analysis

Time Complexity: O(N), where N is the length of A.

Space Complexity: O(N) if you take output into account and O(1) otherwise.

"""



import unittest
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n_squares = []
        p_squares = []
        for num in nums:
            if num < 0:
                n_squares.append(num * num)
            else:
                p_squares.append(num * num)

        idx = 0
        n_ptr = len(n_squares) - 1
        p_ptr = 0

        while n_ptr >= 0 and p_ptr < len(p_squares):
            if n_squares[n_ptr] < p_squares[p_ptr]:
                nums[idx] = n_squares[n_ptr]
                n_ptr -= 1
            else:
                nums[idx] = p_squares[p_ptr]
                p_ptr += 1

            idx += 1

        while n_ptr >= 0:
            nums[idx] = n_squares[n_ptr]
            idx += 1
            n_ptr -= 1

        while p_ptr < len(p_squares):
            nums[idx] = p_squares[p_ptr]
            idx += 1
            p_ptr += 1

        return nums

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.sortedSquares([-4,-1,0,3,10]),[0,1,9,16,100])

    def test_case2(self):
        self.assertEqual(self.obj.sortedSquares([-7,-3,2,3,11]),[4,9,9,49,121])