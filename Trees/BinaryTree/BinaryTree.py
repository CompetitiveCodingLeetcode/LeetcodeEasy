class BinaryTreeNode:
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class BinaryTree:
    def __init__(self, values=None):
        self.root = None
