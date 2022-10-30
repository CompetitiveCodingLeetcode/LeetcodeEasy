"""
Consider lines with a slope of -1 that cross through nodes. Print all diagonal elements in a binary tree that belong to the same line, given a binary tree.

Input : Root of below tree
unnamed

Output :
Diagonal Traversal of binary tree:
 8 10 14
 3 6 7 13
 1 4

APPROACH:
similar to vertical traversal or top view or bottom view. while going left decrement horizontal disatance by 1. while going right don't increment the distance rather keep the same.
"""

class Solution:
    def diagonal_traversal(self,root):
        if root is None:
            return []
        ans = []
        dist_to_node_mapping = {}
        q = []
        q.append((root,(0,0)))
        while len(q) != 0:
            temp = q[0]
            q.pop(0)
            level = temp[1][0]
            horizontal_dist = temp[1][1]
            if horizontal_dist in dist_to_node_mapping.keys():
                dist_to_node_mapping[horizontal_dist].append(temp[0].val)
            else:
                dist_to_node_mapping[horizontal_dist] = [temp[0].val]
            if temp[0].left:
                new_level = level+1
                new_horizontal_dist = horizontal_dist-1
                q.append((temp[0].left,(new_level,new_horizontal_dist)))
            if temp[0].right:
                new_level = level+1
                new_horizontal_dist = horizontal_dist
                q.append((temp[0].right,(new_level,new_horizontal_dist)))
        dist_to_node_mapping = sorted(dist_to_node_mapping.items(),key=lambda x:x[0],reverse=True)
        for item in dist_to_node_mapping:
                ans.append(item[1])
        return ans


