"""
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle, the value of that triangle is the product of the values of its vertices, and the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.



Example 1:


Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:


Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.
Example 3:


Input: values = [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.


Constraints:

n == values.length
3 <= n <= 50
1 <= values[i] <= 100


APPROACH:
Take first and last vertex as I and j respectively. First and last vertex bcoz they will always be adjacent to one another. Now triangles can be formed with other k vertices.
Let k be one of the vertex other than I and j.
So score will be I*k*j + solve for polygon formed with I=i and j=k + solve for polygon formed from I.=k and j=j. Ans would be min of these 2 the earlier ans and what you get after solving the prev.
Base case will be reached when I+1 = j hence return 0 in that case.
Understand the tabulation method.
"""

import sys
from typing import List

class Solution:
    def solve(self, i, j, values):
        if i + 1 == j:
            return 0
        ans = sys.maxsize
        for k in range(i + 1, j):
            ans = min(ans, (values[i] * values[j] * values[k]) + self.solve(i, k, values) + self.solve(k, j, values))
        return ans

    def solveMem(self, i, j, values, ans_store):
        if i + 1 == j:
            return 0
        if ans_store[i][j] != -1:
            return ans_store[i][j]
        ans = sys.maxsize
        for k in range(i + 1, j):
            ans = min(ans,
                      (values[i] * values[j] * values[k]) + self.solveMem(i, k, values, ans_store) + self.solveMem(k, j,
                                                                                                                   values,
                                                                                                                   ans_store))
        ans_store[i][j] = ans
        return ans_store[i][j]

    def minScoreTriangulation(self, values: List[int]) -> int:
        # number_of_vertices = len(values)
        # i = 0
        # j = number_of_vertices-1
        # ans = self.solve(i,j,values)

        number_of_vertices = len(values)
        ans_store = []
        for i in range(0, number_of_vertices):
            temp = []
            for j in range(0, number_of_vertices):
                temp.append(-1)
            ans_store.append(temp)
        i = 0
        j = number_of_vertices - 1
        ans = self.solveMem(i, j, values, ans_store)

        return ans
