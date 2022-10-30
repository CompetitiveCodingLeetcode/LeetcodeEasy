"""
Given a Binary Tree, the task is to print the left view of the Binary Tree. The left view of a Binary Tree is a set of leftmost nodes for every level.

Examples:

Input:
                   4
                /   \
              5     2
                   /   \
                3     1
              /  \
           6    7

Output: 4 5 3 6
Explanation:

left-view

Input:
         1
      /   \
    2       3
      \
       4
         \
          5
            \
             6
Output: 1 2 4 5 6
"""

class Solution:
    def __init__(self):
        self.ans = []

    def solve(self,root,level):
        if root is None:
            return self.ans
        # reached a new level
        if level == len(self.ans):
            self.ans.append(root.val)
        self.solve(root.left,level+1)
        self.solve(root.right,level+1)

    def left_view_of_tree(self,root):
        self.solve(root, 0)
        return self.ans

    def left_view_of_tree_using_level_order_traversal(self,root):
        q = []
        q.append(root)
        while len(q) != 0:
            no_of_nodes_at_level = len(q)
            for i in range(0,no_of_nodes_at_level):
                temp = q[0]
                q.pop(0)
                if i==0:
                    self.ans.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return self.ans

