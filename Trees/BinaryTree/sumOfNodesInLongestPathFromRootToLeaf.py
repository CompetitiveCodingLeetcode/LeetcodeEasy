"""
Given a binary tree containing n nodes. The problem is to find the sum of all nodes on the longest path from root to leaf node. If two or more paths compete for the longest path, then the path having maximum sum of nodes is being considered.
Examples:


Input : Binary tree:
        4
       / \
      2   5
     / \ / \
    7  1 2  3
      /
     6
Output : 13

        4
       / \
      2   5
     / \ / \
    7  1 2  3
      /
     6

The highlighted nodes (4, 2, 1, 6) above are
part of the longest root to leaf path having
sum = (4 + 2 + 1 + 6) = 13

APPROACH:
RECURSIVE APPROACH:
1. for each node store the level and sum from root to that node.
2. Update the max_sum if curr_level val is >= max_level. Store the sum that is max.
3. do updates when you've reached the leaf node.
"""

#Time complexity: O(N)
# Space complexity: O(height)
class Solution:
    def __init__(self):
        self.max_sum = -999999999999
        self.max_len = 0

    def solve(self,root,l_sum,l_len):
        if root is None:
            if l_len > self.max_len:
                self.max_len = l_len
                self.max_sum = l_sum
            elif l_len == self.max_len:
                self.max_sum = max(l_sum,self.max_sum)
            return

        l_sum += root.val
        self.solve(root.left,l_sum,l_len+1)
        self.solve(root.right,l_sum,l_len+1)

    def sum_of_long_root_to_leaf_node(self,root):
        len = 0
        sum = 0

        self.solve(root,sum,len)

        return self.max_sum


