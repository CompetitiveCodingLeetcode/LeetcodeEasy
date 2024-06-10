"""
Given a binary tree. The task is to check whether the given tree follows the max heap property or not.
Note: Properties of a tree to be a max heap - Completeness and Value of node greater than or equal to its child.

Example 1:

Input:
      5
    /  \
   2    3
Output: 1
Explanation: The given tree follows max-heap property since 5,
is root and it is greater than both its children.

Example 2:

Input:
       10
     /   \
    20   30
  /   \
 40   60
Output: 0

Your Task:
You don't need to read input or print anything. Your task is to complete the function isHeap() which takes the root of Binary Tree as parameter returns True if the given binary tree is a heap else returns False.

Expected Time Complexity: O(N)
Expected Space Complexity: O(N)

Constraints:
1 ≤ Number of nodes ≤ 100
1 ≤ Data of a node ≤ 1000

The below solution is giving error in some test cases on gfg. https://www.geeksforgeeks.org/problems/is-binary-tree-heap/1

"""

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:
    def count_nodes(self, root):
        if root == None:
            return 0
        return 1 + self.count_nodes(root.right) + self.count_nodes(root.left)

    def is_complete_binary_tree(self, root, node_count, idx):
        if root == None:
            return True

        if idx >= node_count:
            return False

        return self.is_complete_binary_tree(root.left, node_count, (2 * idx) + 1) and self.is_complete_binary_tree(
            root.right, node_count, (2 * idx) + 2)

    def check_max_order_property(self, root):
        if root.left == None and root.right == None:
            return True

        if root.right == None:
            return root.left.data <= root.data
        else:
            return (root.left.data <= root.data) and (root.right.data <= root.data) and (
                self.check_max_order_property(root.left)) and (self.check_max_order_property(root.right))

    # Your Function Should return True/False
    def isHeap(self, root):
        # Code Here
        num_of_nodes = self.count_nodes(root)
        idx = 0
        is_complete_btree = self.is_complete_binary_tree(root, num_of_nodes, idx)
        has_max_heap_property = self.check_max_order_property(root)

        return is_complete_btree and has_max_heap_property
