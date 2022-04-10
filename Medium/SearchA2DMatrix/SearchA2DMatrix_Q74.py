"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
import unittest
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        start = 0
        end = row * col - 1

        mid = start + (end - start) // 2

        while start <= end:
            element = matrix[mid // col][mid % col]
            if element == target:
                return True
            elif target > element:
                start = mid + 1
            else:
                end = mid - 1
            mid = start + (end - start) // 2

        return False


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertTrue(self.obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))

    def test_case2(self):
        self.assertFalse(self.obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))