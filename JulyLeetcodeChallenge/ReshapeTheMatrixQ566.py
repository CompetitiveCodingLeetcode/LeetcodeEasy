"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]



Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    -1000 <= mat[i][j] <= 1000
    1 <= r, c <= 300


"""
import unittest
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        expected_num_cells = 0
        m = len(mat)
        for i in range(m):
            n = len(mat[i])
            expected_num_cells += n
        if r * c != expected_num_cells:
            return mat
        else:
            elements = []
            for i in range(m):
                for j in range(n):
                    elements.append(mat[i][j])
            temp_count = 0
            row = []
            for i in range(r):
                col = []
                for j in range(c):
                    col.append(elements[temp_count])
                    temp_count += 1
                row.append(col)
            return row


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_success(self):
        self.assertEqual([[1, 2, 3, 4]], self.obj.matrixReshape([[1, 2], [3, 4]], 1, 4))

    def test_failure(self):
        self.assertEqual([[1, 2], [3, 4]], self.obj.matrixReshape([[1, 2], [3, 4]], 2, 4))
