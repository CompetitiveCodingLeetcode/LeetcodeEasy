"""
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node.

Example 1:

Input:
      1
   /    \
  2      3
Output: 2 1 3
Example 2:

Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100
Your Task:
Since this is a function problem. You don't have to take input. Just complete the function topView() that takes root node as parameter and returns a list of nodes visible from the top view from left to right.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 105
1 ≤ Node Data ≤ 105
"""

class Solution:
    def top_view_of_tree(self,root):
        ans = []
        if root is None:
            return ans
        horizontal_distance_to_node_mapping = {}
        q = []
        q.append((root,0))
        while len(q) != 0:
            temp = q[0]
            q.pop(0)
            front_node = temp[0]
            horizontal_distance = temp[1]

            # maintain 1:1 mapping i.e., if one value is present for a horizontal distance then do nothing
            if horizontal_distance not in horizontal_distance_to_node_mapping.keys():
                horizontal_distance_to_node_mapping[horizontal_distance] = front_node.val
            if front_node.left:
                q.append((front_node.left,horizontal_distance-1))
            if front_node.right:
                q.append((front_node.right,horizontal_distance+1))
        print("out of whie loop")
        print(horizontal_distance_to_node_mapping)
        horizontal_distance_to_node_mapping = sorted(horizontal_distance_to_node_mapping.items(),key=lambda x: x[0])
        print(horizontal_distance_to_node_mapping)
        for item in horizontal_distance_to_node_mapping:
            ans.append(item[1])
        return ans