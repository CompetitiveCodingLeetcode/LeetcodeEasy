"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
import unittest
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        row = len(matrix)
        col = len(matrix[0])

        count = 0
        total = row * col

        starting_row = 0
        starting_col = 0
        ending_row = row - 1
        ending_col = col - 1

        ans = []

        while count < total:

            # starting row
            for i in range(starting_col, ending_col + 1):
                if count < total:
                    ans.append(matrix[starting_row][i])
                    count += 1
            starting_row += 1

            # endig col
            for i in range(starting_row, ending_row + 1):
                if count < total:
                    ans.append(matrix[i][ending_col])
                    count += 1
            ending_col -= 1

            # endinng row
            for i in range(ending_col, starting_col - 1, -1):
                if count < total:
                    ans.append(matrix[ending_row][i])
                    count += 1

            ending_row -= 1

            # starting col
            for i in range(ending_row, starting_row - 1, -1):
                if count < total:
                    ans.append(matrix[i][starting_col])
                    count += 1
            starting_col += 1

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]),[1,2,3,6,9,8,7,4,5])

    def test_case2(self):
        self.assertListEqual(self.obj.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]),[1,2,3,4,8,12,11,10,9,5,6,7])