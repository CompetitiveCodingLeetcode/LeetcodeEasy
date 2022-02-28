"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import List
from BinaryTreeNode import BinaryTreeNode


# time complexity = O(n)
# space complexity = O(n)
def helper(root, ans) -> List[int]:
    if root is not None:
        helper(root.left, ans)
        ans.append(root.val)
        helper(root.right, ans)


def inorderTraversal(root: BinaryTreeNode) -> List[int]:
    ans = []
    if root is None:
        return None
    helper(root, ans)
    return ans


# to avoid space complexity one can use Morris Traversal approach as follows:
"""
Approach:
In this method, we have to use a new data structure-Threaded Binary Tree, and the strategy is as follows:

Step 1: Initialize current as root

Step 2: While current is not NULL,

If current does not have left child

    a. Add current’s value

    b. Go to the right, i.e., current = current.right

Else

    a. In current's left subtree, make current the right child of the rightmost node

    b. Go to this left child, i.e., current = current.left
For example:


          1
        /   \
       2     3
      / \   /
     4   5 6

First, 1 is the root, so initialize 1 as current, 1 has left child which is 2, the current's left subtree is

         2
        / \
       4   5
So in this subtree, the rightmost node is 5, then make the current(1) as the right child of 5. Set current = cuurent.left (current = 2). The tree now looks like:

         2
        / \
       4   5
            \
             1
              \
               3
              /
             6
For current 2, which has left child 4, we can continue with thesame process as we did above

        4
         \
          2
           \
            5
             \
              1
               \
                3
               /
              6
then add 4 because it has no left child, then add 2, 5, 1, 3 one by one, for node 3 which has left child 6, do the same as above. Finally, the inorder taversal is [4,2,5,1,6,3].

For more details, please check Threaded binary tree and Explaination of Morris Method

"""

# time complexity = O(n)
# space complexity: O(1)
def inorderTraversal_Morris_traversal(root: BinaryTreeNode) -> List[int]:
    ans = []
    if root is None:
        return None
    curr = root
    while curr is not None:
        if curr.left:
            temp = curr.left
            while temp.right:
                temp = temp.right
            temp.right = curr
            temp2 = curr
            curr = curr.left
            temp2.left = None
        else:
            ans.append(curr.val)
            curr = curr.right
    return ans