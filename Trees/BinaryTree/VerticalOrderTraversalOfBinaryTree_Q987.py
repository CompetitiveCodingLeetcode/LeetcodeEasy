"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:


Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""
from typing import List


class Solution:
    def verticalTraversal(self, root) -> List[List[int]]:
        distance_to_node_mapping = {}
        q = []
        ans = []
        if root is None:
            return ans
        level = 0
        horizontal_distance = 0
        q.append((root,(level,horizontal_distance)))
        while len(q) != 0:
            temp = q[0]
            q.pop(0)
            level = temp[1][0]
            horizontal_distance = temp[1][1]
            if horizontal_distance in distance_to_node_mapping.keys():
                distance_to_node_mapping[horizontal_distance].append(temp[0].val)
            else:
                distance_to_node_mapping[horizontal_distance] = []
                distance_to_node_mapping[horizontal_distance].append(temp[0].val)
            if temp[0].left:
                new_level = level+1
                new_horizontal_distance = horizontal_distance - 1
                q.append((temp[0].left,(new_level,new_horizontal_distance)))
            if temp[0].right:
                new_level = level + 1
                new_horizontal_distance = horizontal_distance + 1
                q.append((temp[0].right,(new_level,new_horizontal_distance)))
            print("q=",q)
        distance_to_node_mapping = sorted(distance_to_node_mapping.items(),key=lambda x: x[0])

        for item in distance_to_node_mapping:
            for i in item[1]:
                ans.append(i)
        return ans

        

