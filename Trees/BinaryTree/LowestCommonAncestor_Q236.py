"""

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

"""


class Solution:
    # time complexity: O(N); Space Complexity: O(N)
    def lowestCommonAncestor(self, root, p, q):
        # base case:
        if root is None:
            print("got none")
            return None
        if root.val == p or root.val == q:
            print("got p or q")
            return root

        left_ans = self.lowestCommonAncestor(root.left,p,q)
        right_ans = self.lowestCommonAncestor(root.right,p,q)

        if left_ans and right_ans:
            print("here")
            return root
        elif left_ans and right_ans is None:
            return left_ans
        elif right_ans and left_ans is None:
            return right_ans
        else:
            return None
