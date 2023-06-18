#time complexity: O(n)
def sum_of_nodes(root) -> int:
    if root == None:
        return 0
    else:

        left_subtree_sum = sum_of_nodes(root.left)
        right_subtree_sum = sum_of_nodes(root.right)

        return left_subtree_sum + right_subtree_sum + root.val