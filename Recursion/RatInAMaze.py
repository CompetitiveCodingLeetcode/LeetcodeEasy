"""
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1},
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at
(3, 3) from (0, 0) by two paths - DRDDRR
and DDRDRR, when printed in sorted order
we get DDRDRR DRDDRR.
Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is
blocked.
Your Task:
You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order.
Note: In case of no path, return an empty list. The driver will output "-1" automatically.

Expected Time Complexity: O((3N^2)).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

Constraints:
2 ≤ N ≤ 5
0 ≤ m[i][j] ≤ 1

"""



import unittest


class Solution:
    def is_safe(self, x, y, m, n, visited):

        if ((x >= 0 and x < n) and (y >= 0 and y < n) and (visited[x][y] == 0) and (m[x][y] == 1)):
            return True
        return False

    def find_possible_paths(self, x, y, m, n, visited, ans, path):
        if x == n - 1 and y == n - 1:
            ans.append(path)
            return

        visited[x][y] = 1

        # 4 paths possible
        # down (x+1)(y)
        # up (x-1)(y)
        # right (x)(y+1)
        # left (x)(y-1)

        # down
        newx = x + 1
        newy = y
        if self.is_safe(newx, newy, m, n, visited):
            path += "D"
            self.find_possible_paths(newx, newy, m, n, visited, ans, path)
            path = path[:-1]

        # up
        newx = x - 1
        newy = y
        if self.is_safe(newx, newy, m, n, visited):
            path += "U"
            self.find_possible_paths(newx, newy, m, n, visited, ans, path)
            path = path[:-1]

        # right
        newx = x
        newy = y + 1
        if self.is_safe(newx, newy, m, n, visited):
            path += "R"
            self.find_possible_paths(newx, newy, m, n, visited, ans, path)
            path = path[:-1]

        # left
        newx = x
        newy = y - 1
        if self.is_safe(newx, newy, m, n, visited):
            path += "L"
            self.find_possible_paths(newx, newy, m, n, visited, ans, path)
            path = path[:-1]

        visited[x][y] = 0

    def findPath(self, m, n):
        # code here

        if m[0][0] == 0:
            return -1

        # initialize visited array
        v = []
        visited = []
        for i in range(0, n):
            for j in range(0, n):
                v.append(0)
            visited.append(v)
            v = []

        ans = []
        path = ""
        x = 0
        y = 0
        visited[x][y] = 1

        self.find_possible_paths(x, y, m, n, visited, ans, path)
        if len(ans) == 0:
            return -1
        return ans

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.obj = Solution()

    def test_case1(self):
        self.assertListEqual(self.obj.findPath([[1, 0, 0, 0],[1, 1, 0, 1],[1, 1, 0, 0],[0, 1, 1, 1]],4),["DDRDRR","DRDDRR"])

    def test_case2(self):
        self.assertEqual(self.obj.findPath([[1,0],[1,0]],2),-1)