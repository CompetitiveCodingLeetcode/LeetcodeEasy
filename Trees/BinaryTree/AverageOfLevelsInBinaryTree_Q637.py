"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from collections import deque
from typing import List

from BinaryTreeNode import BinaryTreeNode

class Solution:
    def averageOfLevels(self, root: BinaryTreeNode) -> List[float]:
        if root == None:
            return 0
        else:
            ans = []
            level_nodes = []
            level_order_traversal_nodes = deque()
            temp = root
            level_order_traversal_nodes.append(temp)
            level_order_traversal_nodes.append(None)
            while len(level_order_traversal_nodes) != 0:
                temp = level_order_traversal_nodes.popleft()
                if temp == None:
                    if len(level_order_traversal_nodes) == 0:
                        avg = sum(level_nodes)/len(level_nodes)
                        ans.append(avg)
                        break
                    level_order_traversal_nodes.append(None)
                    avg = sum(level_nodes)/len(level_nodes)
                    ans.append(avg)
                    level_nodes = []
                else:
                    level_nodes.append(temp.val)
                    if temp.left:
                        level_order_traversal_nodes.append(temp.left)
                    if temp.right:
                        level_order_traversal_nodes.append(temp.right)
            return ans

