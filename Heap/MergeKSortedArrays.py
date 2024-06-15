"""
Given K sorted arrays arranged in the form of a matrix of size K*K. The task is to merge them into one sorted array.
Example 1:

Input:
K = 3
arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
Output: 1 2 3 4 5 6 7 8 9
Explanation:Above test case has 3 sorted
arrays of size 3, 3, 3
arr[][] = [[1, 2, 3],[4, 5, 6],
[7, 8, 9]]
The merged list will be
[1, 2, 3, 4, 5, 6, 7, 8, 9].
Example 2:

Input:
K = 4
arr[][]={{1,2,3,4},{2,2,3,4},
         {5,5,6,6},{7,8,9,9}}
Output:
1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9
Explanation: Above test case has 4 sorted
arrays of size 4, 4, 4, 4
arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4],
[5, 5, 6, 6], [7, 8, 9, 9 ]]
The merged list will be
[1, 2, 2, 2, 3, 3, 4, 4, 5, 5,
6, 6, 7, 8, 9, 9].
Your Task:
You do not need to read input or print anything. Your task is to complete mergeKArrays() function which takes 2 arguments, an arr[K][K] 2D Matrix containing K sorted arrays and an integer K denoting the number of sorted arrays, as input and returns the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python)

Expected Time Complexity: O(K2*Log(K))
Expected Auxiliary Space: O(K2)

Constraints:
1 <= K <= 100

"""
import unittest
from heapq import heappush, heappop


class HeapNode:
    def __init__(self, data, row, col):
        self.data = data
        self.row = row
        self.col = col

    def __lt__(self, nxt):
        return self.data < nxt.data


class Solution:
    # Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        k_min_elements = []
        res = []
        for i in range(0, K):
            row = i
            col = 0
            data = arr[row][col]

            element = HeapNode(data, row, col)
            heappush(k_min_elements, element)

        while len(k_min_elements) > 0:
            row = k_min_elements[0].row
            col = k_min_elements[0].col
            data = k_min_elements[0].data
            heappop(k_min_elements)
            if col + 1 < len(arr[row]):
                heappush(k_min_elements, HeapNode(arr[row][col + 1], row, col + 1))
            res.append(data)
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.obj = Solution()

    def test_case1(self):
        self.assertEqual(self.obj.mergeKArrays([[1,2,3],[4,5,6],[7,8,9]],3),[1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_case2(self):
        self.assertEqual(self.obj.mergeKArrays([[1,2,3,4],[2,2,3,4],[5,5,6,6],[7,8,9,9]],4),[1, 2, 2, 2, 3, 3, 4, 4, 5, 5,6, 6, 7, 8, 9, 9])