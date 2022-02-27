
def height_of_tree(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return 1 + max(height_of_tree(root.left),height_of_tree(root.right))


