"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:

        3
    9       20
        15      7
Input: root = [3,9,20,null,null,15,7]
Output: true


Example 2:

            1
        2           2
    3      3
4      4
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from HeightOfTree import height_of_tree

class TreeInfo:
    def __init__(self,is_balanced,height):
        self.is_balanced = is_balanced
        self.height = height

class Solution:
    # Time complexity: O(n^2)
    def isBalanced(self, root) -> bool:
        # to check whether a tree is balanced or not
        if root is None or (root.left is None and root.right is None):
            return True
        else:
            left_ans = self.isBalanced(root.left)
            right_ans = self.isBalanced(root.right)
            curr_ans = abs(height_of_tree(root.left)-height_of_tree(root.right)) <= 1
            # print("curr_ans====",curr_ans)
            if left_ans and right_ans and curr_ans:
                return True
            else:
                return False

    # Time complexity: O(n)
    def is_balanced_optimized(self,root):
        if root is None:
            return TreeInfo(True,0)
        elif root.left is None and root.right is None:
            return TreeInfo(True,1)
        else:
            left_ans = self.is_balanced_optimized(root.left)
            right_ans = self.is_balanced_optimized(root.right)
            curr_ans = abs(left_ans.height-right_ans.height) <= 1

            if left_ans.is_balanced and right_ans.is_balanced and curr_ans:
                return TreeInfo(True,max(left_ans.height,right_ans.height))
            else:
                return TreeInfo(False,max(left_ans.height,right_ans.height))




