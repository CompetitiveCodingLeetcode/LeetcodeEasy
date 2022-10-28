"""
Write a function that returns true if the given Binary Tree is SumTree else false. A SumTree is a Binary Tree where the value of a node is equal to the sum of the nodes present in its left subtree and right subtree. An empty tree is SumTree and the sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.

Following is an example of SumTree.

          26
        /   \
      10     3
    /    \     \
  4      6      3
"""

class TreeInfo:
    def __init__(self,is_sum_tree,tree_sum):
        self.is_sum_tree = is_sum_tree
        self.tree_sum = tree_sum

class Solution:
    def is_sum_tree(self,root):
        if root is None:
            return TreeInfo(True,0)
        elif root.left is None and root.right is None:
            return TreeInfo(True,root.val)
        else:
            left_ans = self.is_sum_tree(root.left)
            right_ans = self.is_sum_tree(root.right)
            curr_sum = left_ans.tree_sum + right_ans.tree_sum
            # print("root val=",root.val)
            # print("curr_sum == ",curr_sum)
            curr_ans = root.val == curr_sum
            # print("curr_ans===",curr_ans)

            if left_ans.is_sum_tree and right_ans.is_sum_tree and curr_ans:
                return TreeInfo(True,curr_sum+root.val)
            else:
                return TreeInfo(False,curr_sum+root.val)


