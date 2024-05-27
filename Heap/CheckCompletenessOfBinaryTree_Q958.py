"""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:


Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.


Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000

TODO: make a running code
"""


class Solution:
    def count_nodes(self, root):
        if root == None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def is_complete(self, root, idx, node_count):
        if root == None:
            return True

        if idx >= node_count:
            return False

        return self.is_complete(root.left, (2 * idx) + 1, node_count) and self.is_complete(root.right, (2 * idx) + 2,
                                                                                           node_count)

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        num_of_nodes = self.count_nodes(root)
        idx = 0
        return self.is_complete(root, idx, num_of_nodes)
