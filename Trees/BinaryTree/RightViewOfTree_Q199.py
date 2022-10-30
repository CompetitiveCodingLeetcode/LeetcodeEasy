"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
    def rightSideView(self, root) -> List[int]:
        if root is None:
            return []
        q = []
        q.append(root)
        ans = []
        while len(q) !=0:
            size = len(q)
            for i in range(0,size):
                temp = q[0]
                q.pop(0)
                if i == size-1:
                    ans.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return ans

    def solve(self,root,level):
        if root is None:
            return self.ans

        if level == len(self.ans):
            self.ans.append(root.val)

        self.solve(root.right,level+1)
        self.solve(root.left,level+1)

    def right_view_using_recursion(self,root):
        self.solve(root,0)
        return self.ans