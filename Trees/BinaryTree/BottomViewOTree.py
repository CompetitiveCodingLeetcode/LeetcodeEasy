"""
Given a Binary Tree, The task is to print the bottom view from left to right. A node x is there in output if x is the bottommost node at its horizontal distance. The horizontal distance of the left child of a node x is equal to a horizontal distance of x minus 1, and that of a right child is the horizontal distance of x plus 1.

Examples:

Input:            20
                    /     \
                8         22
             /      \         \
          5         3        25
                   /    \
              10       14

Output: 5, 10, 3, 14, 25.

Input:              20
                    /     \
                8         22
             /     \     /     \
          5        3  4      25
                  /    \
              10       14
Output: 5 10 4 14 25.
Explanation: If there are multiple bottom-most nodes for a horizontal distance from the root, then print the later one in the level traversal. 3 and 4 are both the bottom-most nodes at a horizontal distance of 0, we need to print 4.
"""

class Solution:
    # infinite loop
    def bottom_view_of_tree(self,root):
        ans = []
        if root is None:
            return ans
        horizontal_distance_to_node_mapping = {}
        q = []
        q.append((root,0))
        while len(q) != 0:
            temp = q[0]
            q.pop()
            front_node = temp[0]
            horizontal_distance = temp[1]

            horizontal_distance_to_node_mapping[horizontal_distance] = front_node.val
            if front_node.left:
                q.append((front_node.left,horizontal_distance-1))
            if front_node.right:
                q.append((front_node.right,horizontal_distance+1))
        print("out of whie loop")
        sorted(horizontal_distance_to_node_mapping,key=horizontal_distance_to_node_mapping.keys())
        for key,val in horizontal_distance_to_node_mapping.items():
            ans.append(val)
        return ans