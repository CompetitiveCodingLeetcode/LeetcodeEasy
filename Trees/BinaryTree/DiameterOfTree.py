"""
Diameter of tree is the number of nodes in the longest path between any 2 nodes

case1: Diameter through root node

            2
    3           6
4       5          8


case 2: diameter not through root node

            2
        3
    5       6
      1   7
            8

in this case there are further two cases: diameter lies in left subtree or diameter lies in right subtree

hence we can conclude that for a nnode:
diam1  = max diameter of left subtree
diam2 = max diameter of right subtree
diam3 = height of left subtree + height of right subtree + 1

final diam = max(diam3,max(diam1,diam2))

"""
from HeightOfTree import height_of_tree


class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


# time complexity: O(n^2)
def find_diameter(root):
    if root is None:
        return 0
    diam1 = find_diameter(root.left)
    diam2 = find_diameter(root.right)
    diam3 = height_of_tree(root.left) + height_of_tree(root.right) + 1

    return max(diam3, max(diam1, diam2))


#time complexity : O(n)
def find_diameter_optimized_approach(root) -> TreeInfo:
    if root is None:
        return TreeInfo(0, 0)

    left = find_diameter_optimized_approach(root.left)
    right = find_diameter_optimized_approach(root.right)

    my_height = max(left.height, right.height) + 1

    diam1 = left.diameter
    diam2 = right.diameter
    diam3 = left.height + right.height + 1

    my_diameter = max(max(diam1, diam2), diam3)

    my_info = TreeInfo(my_height, my_diameter)
    return my_info
