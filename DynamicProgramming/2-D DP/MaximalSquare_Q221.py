"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.


APPROACH:

"""


class Solution:
    # def solve(self,matrix,i,j,max_size):
    #     if (i >= len(matrix)) or (j >= len(matrix[0])):
    #         return 0

    #     diag = self.solve(matrix,i+1,j+1,max_size)
    #     right = self.solve(matrix,i,j+1,max_size)
    #     bottom = self.solve(matrix,i+1,j,max_size)

    #     if matrix[i][j] == "1":
    #         ans = 1 + min(diag,right,bottom)
    #         max_size[0] = max(ans,max_size[0])
    #         print("max size ===",max_size)
    #         return ans
    #     else:
    #         return 0

    # def solveMem(self,matrix,i,j,max_size,ans_store):
    #     if (i >= len(matrix)) or (j >= len(matrix[0])):
    #         return 0

    #     if ans_store[i][j] != -1:
    #         return ans_store[i][j]

    #     right = self.solveMem(matrix,i,j+1,max_size,ans_store)
    #     diag = self.solveMem(matrix,i+1,j+1,max_size,ans_store)
    #     bottom = self.solveMem(matrix,i+1,j,max_size,ans_store)

    #     if matrix[i][j] == "1":
    #         ans_store[i][j] = 1 + min(diag,right,bottom)
    #         max_size[0] = max(ans_store[i][j],max_size[0])
    #         return ans_store[i][j]
    #     else:
    #         ans_store[i][j] = 0
    #         return ans_store[i][j]

    def solveTab(self, matrix, max_square_size):
        ans_store = []

        for i in range(0, len(matrix) + 1):
            temp = []
            for j in range(0, len(matrix[0]) + 1):
                temp.append(0)
            ans_store.append(temp)

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                right = ans_store[i][j + 1]
                diag = ans_store[i + 1][j + 1]
                bottom = ans_store[i + 1][j]

                if matrix[i][j] == "1":
                    ans_store[i][j] = 1 + min(min(diag, right), bottom)
                    max_square_size[0] = max(ans_store[i][j], max_square_size[0])
                elif matrix[i][j] == "0":
                    ans_store[i][j] = 0
        return ans_store[0][0]

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square_size = [0]
        i=0
        j=0
        self.solve(matrix,i,j,max_square_size)
        print("max square size==",max_square_size)

        # max_square_size=[0]
        # max_square_size_store = [[-1]*(len(matrix[0]))]*(len(matrix))
        # self.solveMem(matrix,0,0,max_square_size,max_square_size_store)
        # return max_square_size[0] * max_square_size[0]

        max_square_size = [0]
        self.solveTab(matrix, max_square_size)
        return max_square_size[0] * max_square_size[0]
