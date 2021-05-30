"""
https://leetcode.com/problems/rotate-image/
"""
import unittest
from typing import List


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    for i in range(len(matrix)):
        for j in range(i + 1):
            if i != j:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
    return matrix


def reverse_rows_of_matrix(matrix: List[List[int]]) -> List[List[int]]:
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix


def rotate_image_by_90_degrees(matrix: List[List[int]]) -> List[List[int]]:
    matrix = transpose_matrix(matrix)

    matrix = reverse_rows_of_matrix(matrix)

    return matrix


class TestSolution(unittest.TestCase):
    def test_transpose_matrix(self):
        self.assertListEqual([[1, 4, 7], [2, 5, 8], [3, 6, 9]], transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_reverse_rows_of_matrix(self):
        self.assertListEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]],
                             reverse_rows_of_matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))

    def test_rotate_image_by_90_degrees(self):
        self.assertListEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]],
                             rotate_image_by_90_degrees([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
