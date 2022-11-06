"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from typing import List


class Solution:
    def __init__(self):
        self.ans= []
        self.node_to_leaf_sum = 0

    def solve(self,root,target_sum,temp_ans):
        if root is None:
            return
        if root.left  is None and root.right is None:
            self.node_to_leaf_sum += root.val
            temp_ans.append(root.val)
            if self.node_to_leaf_sum == target_sum:
                self.ans.append(temp_ans.copy())
                self.node_to_leaf_sum -= root.val
                temp_ans.pop(-1)
            else:
                self.node_to_leaf_sum -= root.val
                temp_ans.pop(-1)
        else:
            self.node_to_leaf_sum += root.val
            temp_ans.append(root.val)
            self.solve(root.left,target_sum,temp_ans)
            self.solve(root.right,target_sum,temp_ans)
            self.node_to_leaf_sum -= root.val
            temp_ans.pop(-1)

    def pathSum(self, root, targetSum: int) -> List[List[int]]:
        temp_ans = []
        self.solve(root,targetSum,temp_ans)
        return self.ans